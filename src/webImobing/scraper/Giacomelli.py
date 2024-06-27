from src.webImobing.Constants import Constants
from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration
from src.webImobing.utils.Logger import logger
from src.webImobing.utils.UrlBuilder import UrlBuilder


class Giacomelli(GenericScraper):
    IDENTIFIER = Constants.GIACOMELLI

    def __init__(self, config: ScraperConfiguration):
        super().__init__(config)
        self.url_builder = UrlBuilder()

    def run(self):
        logger.info(f"Rodando o scraper {self.IDENTIFIER}")
        self.url_builder.add_base_url(Constants.URL_BASE[self.IDENTIFIER])
        self.add_endpoints()
        self.add_params()
        url = self.url_builder.build()
        logger.info(f"URL da {self.IDENTIFIER} a ser raspado: {url}")
        logger.error(f"Não foi possível fazer scraping da Giacomelli, pois as informações são carregadas "
                     f"dinamicamente, por javascript.")
        logger.info(f"Finalizando o scraper {self.IDENTIFIER}")

    def add_endpoints(self):
        self.url_builder.add_endpoint("imoveis").add_endpoint("residencial").add_endpoint("florianopolis")

        for key, value in self.config.get_params().items():
            # Valores -1 são ignorados
            if value == -1:
                continue

    def add_params(self):
        pass