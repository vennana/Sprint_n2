import pytest

from data.test_data import CATEGORIES, DEFAULT_AD


class TestCreateAd:

    def test_create_ad_success(self, ads_api, registered_user):
        response = ads_api.create_ad(registered_user["token"], DEFAULT_AD)

        assert response.status_code == 201
        body = response.json()
        assert body["name"] == DEFAULT_AD["name"]
        assert body["category"] == DEFAULT_AD["category"]
        assert body["city"] == DEFAULT_AD["city"]
        assert body["price"] == int(DEFAULT_AD["price"])
        assert "id" in body

    @pytest.mark.parametrize("category", CATEGORIES)
    def test_create_ad_in_each_category(
        self, ads_api, registered_user, category
    ):
        ad_data = dict(DEFAULT_AD, category=category)

        response = ads_api.create_ad(registered_user["token"], ad_data)

        assert response.status_code == 201
        assert response.json()["category"] == category