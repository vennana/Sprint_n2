from data.test_data import UPDATED_AD, MSG_NO_RIGHTS_TO_EDIT


class TestEditAd:

    def test_edit_own_ad_success(self, ads_api, registered_user, created_ad):
        response = ads_api.update_ad(
            registered_user["token"], created_ad, UPDATED_AD
        )

        assert response.status_code == 200
        body = response.json()
        assert body["id"] == created_ad
        assert body["name"] == UPDATED_AD["name"]
        assert body["category"] == UPDATED_AD["category"]
        assert body["city"] == UPDATED_AD["city"]
        assert body["price"] == int(UPDATED_AD["price"])

    def test_edit_foreign_ad_fails(
        self, ads_api, second_registered_user, created_ad
    ):
        response = ads_api.update_ad(
            second_registered_user["token"], created_ad, UPDATED_AD
        )

        assert response.status_code == 401
        body = response.json()
        assert body["statusCode"] == 401
        assert body["error"] == "Unauthorized"
        assert body["message"] == MSG_NO_RIGHTS_TO_EDIT