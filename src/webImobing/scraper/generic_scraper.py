from src.webImobing.configuration import Configuration


class GenericScraper:
    def __init__(self, config: Configuration):
        self.config = config.scraper_config
