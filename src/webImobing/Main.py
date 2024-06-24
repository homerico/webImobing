import sys

from Configuration import Configuration

if __name__ == '__main__':
    if len(sys.argv) == 1:
        conf = Configuration("default.json")
    else:
        conf = Configuration(sys.argv[1])

    configured_scrapers = []
    for scraper_id in conf.scraper_ids:
        configured_scrapers.append(conf.SCRAPER_INSTANCES[scraper_id](conf.get_scraper_configuration()))

    # TODO: Paralelizar a execução dos scraper
    for scraper in configured_scrapers:
        scraper.run()
