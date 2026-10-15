import pytest

from api.ads_api import AdsAPI
from api.auth_api import AuthAPI
from data.email_generator import generate_email
from data.test_data import DEFAULT_PASSWORD, DEFAULT_AD


@pytest.fixture
def auth_api() -> AuthAPI:
    return AuthAPI()


@pytest.fixture
def ads_api() -> AdsAPI:
    return AdsAPI()


@pytest.fixture
def registered_user(auth_api):
    email = generate_email()
    response = auth_api.signup(email, DEFAULT_PASSWORD)
    token = auth_api.extract_token_from_signup(response)
    return {"email": email, "password": DEFAULT_PASSWORD, "token": token}


@pytest.fixture
def second_registered_user(auth_api):
    email = generate_email()
    response = auth_api.signup(email, DEFAULT_PASSWORD)
    token = auth_api.extract_token_from_signup(response)
    return {"email": email, "password": DEFAULT_PASSWORD, "token": token}


@pytest.fixture
def created_ad(ads_api, registered_user):
    response = ads_api.create_ad(registered_user["token"], DEFAULT_AD)
    ad_id = response.json()["id"]
    yield ad_id
    ads_api.delete_ad(registered_user["token"], ad_id)