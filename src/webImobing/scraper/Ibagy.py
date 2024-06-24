from src.webImobing.Constants import Constants
from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.utils.Logger import logger


class Ibagy(GenericScraper):
    IDENTIFIER = Constants.IBAGY

    def run(self):
        logger.warn(f"O scraper {self.IDENTIFIER} ainda não foi implementado")