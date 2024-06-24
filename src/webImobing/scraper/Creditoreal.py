from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.utils.Logger import logger
from src.webImobing.Constants import Constants


class CreditoReal(GenericScraper):
    IDENTIFIER = Constants.CREDITOREAL

    def run(self):
        logger.warn(f"O scraper {self.IDENTIFIER} ainda não foi implementado")