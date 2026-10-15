from api.base_api import BaseAPI
from data.test_data import SIGNUP_ENDPOINT, SIGNIN_ENDPOINT

class AuthAPI(BaseAPI):

    def signup(self, email: str, password: str):
        payload = {
            "email": email,
            "password": password,
            "submitPassword": password,
        }
        return self._request("POST", SIGNUP_ENDPOINT, json=payload)

    def signin(self, email: str, password: str):
        payload = {"email": email, "password": password}
        return self._request("POST", SIGNIN_ENDPOINT, json=payload)

    @staticmethod
    def extract_token_from_signup(response) -> str:
        return response.json()["access_token"]["access_token"]

    @staticmethod
    def extract_token_from_signin(response) -> str:
        return response.json()["token"]["access_token"]