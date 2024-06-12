import json
import os


class FileHandler:
    @staticmethod
    def save_file(file, path):
        with open(path, 'wb') as f:
            f.write(file)

    @staticmethod
    def read_file(path):
        with open(path, 'rb') as f:
            return f.read()

    @staticmethod
    def remove_file(path):
        os.remove(path)

    @staticmethod
    def load_settings(target):
        settings_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "settings")
        file_path = os.path.join(settings_dir, target)

        return json.load(open(file_path, 'r'))
