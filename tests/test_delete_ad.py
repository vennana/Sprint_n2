from data.test_data import MSG_AD_DELETED

class TestDeleteAd:

    def test_delete_own_ad_success(self, ads_api, registered_user, created_ad):
        response = ads_api.delete_ad(registered_user["token"], created_ad)

        assert response.status_code == 200
        assert response.json()["message"] == MSG_AD_DELETED