import requests

from data.test_data import BASE_URL

class BaseAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        return self.session.request(method, f"{BASE_URL}{endpoint}", **kwargs)