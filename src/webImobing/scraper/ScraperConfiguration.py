class ScraperConfiguration:
    params = dict()

    def add_param(self, key, value):
        self.params[key] = value

    def get(self, key):
        return self.config[key]

    def get_params(self):
        return self.params
