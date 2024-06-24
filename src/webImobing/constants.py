from src.webImobing.scraper.creditoreal import CreditoReal
from src.webImobing.scraper.giancomelli import Giancomelli
from src.webImobing.scraper.ibagy import Ibagy
from src.webImobing.scraper.olx import Olx


class Constants:
    OLX = "olx"
    IBAGY = "ibagy"
    CREDITOREAL = "creditoreal"
    GIANCOMELLI = "giancomelli"

    SCRAPER_INSTANCES = {
         OLX          : Olx,
         IBAGY        : Ibagy,
         CREDITOREAL  : CreditoReal,
         GIANCOMELLI  : Giancomelli
    }

    URL_BASE = {
        OLX          : "https://www.olx.com.br/imoveis",
        IBAGY        : "https://www.ibagy.com.br/imoveis",
        CREDITOREAL  : "https://www.creditoreal.com.br/imoveis",
        GIANCOMELLI  : "https://www.giancomelli.com.br/imoveis"
    }

    PARAMS_MAP = {
        OLX          : {
            "val_min" : 0,
            "val_max" : 2000,
            "tipos" : ["apartamento"],
            "estado" : "SC",
            "cidade" : "Florianópolis",
            "bairros" : ["Trindade"],
            "area_min" : 0,
            "area_max" : -1,
            "quartos_min" : 0,
            "quartos_max" : -1,
            "banheiros_min" : 0,
            "banheiros_max" : -1,
            "vagas_min" : 1,
            "vagas_max" : -1
        },
        IBAGY        : {
            "val_min" : 0,
            "val_max" : 2000,
            "tipos" : ["apartamento"],
            "estado" : "SC",
            "cidade" : "Florianópolis",
            "bairros" : ["Trindade"],
            "area_min" : 0,
            "area_max" : -1,
            "quartos_min" : 0,
            "quartos_max" : -1,
            "banheiros_min" : 0,
            "banheiros_max" : -1,
            "vagas_min" : 1,
            "vagas_max" : -1
        },
        CREDITOREAL  : {
            "val_min" : 0,
            "val_max" : 2000,
            "tipos" : ["apartamento"],
            "estado" : "SC",
            "cidade" : "Florianópolis",
            "bairros" : ["Trindade"],
            "area_min" : 0,
            "area_max" : -1,
            "quartos_min" : 0,
            "quartos_max" : -1,
            "banheiros_min" : 0,
            "banheiros_max" : -1,
            "vagas_min" : 1,
            "vagas_max" : -1
        },
        GIANCOMELLI  : {
            "val_min" : 0,
            "val_max" : 2000,
            "tipos" : ["apartamento"],
            "estado" : "SC",
            "cidade" : "Florianópolis",
            "bairros" : ["Trindade"],
            "area_min" : 0,
            "area_max" : -1,
            "quartos_min" : 0,
            "quartos_max" : -1,
            "banheiros_min" : 0,
            "banheiros_max" : -1,
            "vagas_min" : 1,
            "vagas_max" : -1
        }
    }