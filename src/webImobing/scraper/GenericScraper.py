from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration


class GenericScraper:
    def __init__(self, config: ScraperConfiguration):
        self.config = config

    def run(self):
        pass

    def add_endpoints(self):
        pass

    def add_params(self):
        pass
