
class UrlBuilder:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint}"