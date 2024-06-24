from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration
from src.webImobing.utils.UrlBuilder import UrlBuilder


class GenericScraper:
    def __init__(self, config: ScraperConfiguration):
        self.config = config
        self.url_builder = UrlBuilder()

    def run(self):
        pass

    def add_endpoints(self):
        pass

    def add_params(self):
        pass
