import sys

from configuration import Configuration
from src.webImobing.constants import Constants

if __name__ == '__main__':
    if len(sys.argv) == 1:
        conf = Configuration("default.json")
    else:
        conf = Configuration(sys.argv[1])

    scrapers = []
    for scraper in conf.scrapers:
        scrapers.append(Constants.SCRAPER_INSTANCES[scraper](conf))
