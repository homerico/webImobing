
class UrlBuilder:
    DIRECTORY_DELIMITER = "/"
    QUERY_DELIMITER = "?"
    PARAM_DELIMITER = "&"

    # O params será uma list de dict
    params = list()
    endpoints = list()

    def add_base_url(self, base_url: str):
        self.base_url = base_url
        return self

    def add_endpoint(self, endpoint: str):
        self.endpoints.append(endpoint)
        return self

    def insert_endpoint(self, endpoint: str, position: int):
        self.endpoints.insert(position, endpoint)
        return self

    def add_param(self, param: str, value):
        self.params.append({param: value})
        return self

    def insert_param(self, param: str, position: int, value):
        self.params.insert(position, {param: value})
        return self

    def build(self):
        url = (self.base_url +
               self.DIRECTORY_DELIMITER +
               self.DIRECTORY_DELIMITER.join(self.endpoints) +
               self.QUERY_DELIMITER +
               self.PARAM_DELIMITER.join(
                   [f"{list(param.keys())[0]}={list(param.values())[0]}" for param in self.params]))

        return url
