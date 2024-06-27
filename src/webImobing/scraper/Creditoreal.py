import hashlib
import json

import requests
from bs4 import BeautifulSoup

from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration
from src.webImobing.utils.FileHandler import FileHandler
from src.webImobing.utils.Logger import logger
from src.webImobing.Constants import Constants
from src.webImobing.utils.UrlBuilder import UrlBuilder


class CreditoReal(GenericScraper):
    IDENTIFIER = Constants.CREDITOREAL

    def __init__(self, config: ScraperConfiguration):
        super().__init__(config)
        self.url_builder = UrlBuilder()
        self.params = dict()

    def run(self):
        logger.info(f"Rodando o scraper {self.IDENTIFIER}")
        self.url_builder.add_base_url(Constants.URL_BASE[self.IDENTIFIER])
        self.add_endpoints()
        self.add_params()
        url = self.url_builder.build()
        logger.info(f"URL da {self.IDENTIFIER} a ser raspado: {url}")

        unprocessed_data = self.scrap(url)
        logger.info(f"Quantidade de dados não processados: {len(unprocessed_data)}")

        data = self.process_data(unprocessed_data)
        logger.info(f"Quantidade de dados processados: {len(data)}")

        self.save_data(data)

        logger.info(f"Finalizando o scraper {self.IDENTIFIER}")

    def add_endpoints(self):
        self.url_builder.add_endpoint("alugueis")

    def add_params(self):
        filters = dict()
        filters["valueType"] = True
        filters["cityState"] = "Florianópolis_SC"

        for key, value in self.config.get_params().items():
            if value == -1:
                continue

            if key == "tipos":
                filters[Constants.PARAMS_MAP[self.IDENTIFIER][key]] = [Constants.PARAMS_MAP[self.IDENTIFIER][val] for val in value]
            else:
                filters[Constants.PARAMS_MAP[self.IDENTIFIER][key]] = value

        self.params["filters"] = json.dumps(filters)

    def scrap(self, url):
        response = requests.get(url, params=self.params)
        casas = []

        if response.status_code == 200:
            logger.info(f"Status code da resposta da requisição: {response.status_code}")

            site = BeautifulSoup(response.content, 'html.parser')
            casas.extend(site.findAll(class_="sc-613ef922-1 iJQgSL"))
            ultima_pagina = site.findAll(class_="sc-32c77bca-3 hglxVa")
            ultima_pagina = int(ultima_pagina[-1].text) if len(ultima_pagina) > 0 else 1

            for i in range(2, ultima_pagina + 1):
                self.params["page"] = i
                response = requests.get(url, params=self.params)
                site = BeautifulSoup(response.content, 'html.parser')
                casas.extend(site.findAll(class_="sc-613ef922-1 iJQgSL"))

            return casas
        else:
            logger.error(f"Erro ao fazer a requisição: {response.status_code}, na URL: {url}")
            return casas

    def process_data(self, unprocessed_data):
        processed_data = dict()
        for casa in unprocessed_data:
            url = casa["href"]

            aux = casa.findAll("p")
            area = aux[0].text
            quartos = aux[1].text
            vagas = aux[2].text if len(aux) == 4 else 0
            preco = aux[3].text if len(aux) == 4 else aux[2].text

            endereco = casa.find(class_="sc-b308a2c-1 XuQTN").findAll("span")
            rua = endereco[0].text
            bairro = endereco[1].text

            id = hashlib.sha256(url.encode()).hexdigest()

            processed_data[id] = {
                "url": url,
                "area": area,
                "quartos": quartos,
                "vagas": vagas,
                "preco": preco,
                "rua": rua,
                "bairro": bairro
            }

        return processed_data

    def save_data(self, data):
        file_handler = FileHandler()
        file_handler.save_scraped_data(f"{self.IDENTIFIER}.json", data)
