from src.webImobing.utils.file_handler import FileHandler
from utils.logger import logger


class Configuration:
    def __init__(self, file_name: str):
        raw_config = FileHandler.load_settings(file_name)

        self.scraper_ids = []
        self.scraper_config = {}
        for key, value in raw_config.items():
            if key == "imobiliarias":
                self.scraper_ids = value
            else:
                self.scraper_config[key] = value

        logger.info(f"Os scrapers serão criados com a configuração extraída do arquivo {file_name}")
