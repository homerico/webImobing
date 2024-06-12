import json
import os

from utils.logger import logger

class Configuration:
    def __init__(self, file_name):
        settings_dir = os.path.join(os.path.dirname(__file__), "..", "..", "settings")
        file_path = os.path.join(settings_dir, file_name)

        logger.info(f"Classe Configuration criada usando o arquivo {file_name}")

        self.config = json.load(open(file_path, 'r'))
        logger.debug(f"Configuração carregada: \n{self.config}")
