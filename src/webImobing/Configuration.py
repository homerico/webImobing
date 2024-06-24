from src.webImobing.scraper.ScraperConfiguration import ScraperConfiguration
from src.webImobing.utils.FileHandler import FileHandler
from utils.Logger import logger
from src.webImobing.scraper.Creditoreal import CreditoReal
from src.webImobing.scraper.Giancomelli import Giancomelli
from src.webImobing.scraper.Ibagy import Ibagy
from src.webImobing.scraper.Olx import Olx


class Configuration:
    SCRAPER_INSTANCES = {
        Olx.IDENTIFIER: Olx,
        Ibagy.IDENTIFIER: Ibagy,
        CreditoReal.IDENTIFIER: CreditoReal,
        Giancomelli.IDENTIFIER: Giancomelli
    }

    scraper_config = ScraperConfiguration()

    def __init__(self, file_name: str):
        raw_config = FileHandler.load_settings(file_name)

        self.scraper_ids = []
        for key, value in raw_config.items():
            if key == "imobiliarias":
                self.scraper_ids = value
            else:
                self.scraper_config.add_param(key, value)

        logger.info(f"Os scrapers serão criados com a configuração extraída do arquivo {file_name}")

    def get_scraper_configuration(self):
        return self.scraper_config
