from src.webImobing.Constants import Constants
from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.utils.Logger import logger


class Olx(GenericScraper):
    IDENTIFIER = Constants.OLX

    def run(self):
        logger.info(f"Rodando o scraper {self.IDENTIFIER}")
        self.url_builder.add_base_url(Constants.URL_BASE[self.IDENTIFIER])
        self.add_endpoints()
        self.add_params()
        url = self.url_builder.build()
        logger.info(f"URL da {self.IDENTIFIER} a ser raspado: {url}")

    def add_endpoints(self):
        self.url_builder.add_endpoint("imoveis").add_endpoint("aluguel").add_endpoint("estado-sc").add_endpoint("florianopolis-e-regiao")

    def add_params(self):
        for key, value in self.config.get_params().items():
            # Valores -1 são ignorados
            if value == -1:
                continue

            if key == "tipos":
                for tipo in value:
                    self.url_builder.add_param(Constants.PARAMS_MAP[self.IDENTIFIER][key],
                                               Constants.PARAMS_MAP[self.IDENTIFIER][tipo])
            elif (value >= 5 and (key == "banheiros_max" or key == "banheiros_min" or
                                  key == "quartos_max" or key == "quartos_min" or key == "vagas")):
                self.url_builder.add_param(Constants.PARAMS_MAP[self.IDENTIFIER][key], "5")
            elif key == "area_max" or key == "area_min":
                for mapped_area, area in enumerate(Constants.AREA_INTERVALS_OLX):
                    if value <= area:
                        self.url_builder.add_param(Constants.PARAMS_MAP[self.IDENTIFIER][key], mapped_area)
                        break
            else:
                self.url_builder.add_param(Constants.PARAMS_MAP[self.IDENTIFIER][key], value)
