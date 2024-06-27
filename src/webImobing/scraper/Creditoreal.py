from src.webImobing.scraper.GenericScraper import GenericScraper
from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration
from src.webImobing.utils.Logger import logger
from src.webImobing.Constants import Constants
from src.webImobing.utils.UrlBuilder import UrlBuilder


class CreditoReal(GenericScraper):
    IDENTIFIER = Constants.CREDITOREAL

    def __init__(self, config: ScraperConfiguration):
        super().__init__(config)
        self.url_builder = UrlBuilder()

    def run(self):
        logger.warn(f"O scraper {self.IDENTIFIER} ainda não foi implementado")