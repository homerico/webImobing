class Constants:
    # Identificadores dos scrapers
    OLX = "olx"
    IBAGY = "ibagy"
    CREDITOREAL = "creditoreal"
    GIANCOMELLI = "giancomelli"

    # URL base dos sites
    URL_BASE = {
        OLX: "https://www.olx.com.br",
        IBAGY: "https://www.ibagy.com.br",
        CREDITOREAL: "https://www.creditoreal.com.br",
        GIANCOMELLI: "https://www.giancomelli.com.br"
    }

    # Intervalos de valores da área na OLX
    AREA_INTERVALS_OLX = [0, 30, 60, 90, 120, 150, 180, 200, 250, 300, 400, 500]

    # Mapeamento dos parâmetros dos links
    PARAMS_MAP = {
        OLX: {
            "tipos": "ret",
            "apartamento": "1020",
            "casa": "1040",
            "quarto": "1060",
            "val_min": "ps",
            "val_max": "pe",
            "area_min": "ss",
            "area_max": "se",
            "quartos_min": "ros",
            "quartos_max": "roe",
            "banheiros_min": "bas",
            "banheiros_max": "bae",
            "vagas": "gsp"
        },
        IBAGY: {
            "val_min": 0,
            "val_max": 2000,
            "tipos": ["apartamento"],
            "area_min": 0,
            "area_max": -1,
            "quartos_min": 0,
            "quartos_max": -1,
            "banheiros_min": 0,
            "banheiros_max": -1,
            "vagas_min": 1,
            "vagas_max": -1
        },
        CREDITOREAL: {
            "val_min": 0,
            "val_max": 2000,
            "tipos": ["apartamento"],
            "area_min": 0,
            "area_max": -1,
            "quartos_min": 0,
            "quartos_max": -1,
            "banheiros_min": 0,
            "banheiros_max": -1,
            "vagas_min": 1,
            "vagas_max": -1
        },
        GIANCOMELLI: {
            "val_min": 0,
            "val_max": 2000,
            "tipos": ["apartamento"],
            "area_min": 0,
            "area_max": -1,
            "quartos_min": 0,
            "quartos_max": -1,
            "banheiros_min": 0,
            "banheiros_max": -1,
            "vagas_min": 1,
            "vagas_max": -1
        }
    }
