from requests_toolbelt import MultipartEncoder

from api.base_api import BaseAPI
from data.test_data import (
    CREATE_LISTING_ENDPOINT,
    UPDATE_OFFER_ENDPOINT,
    DELETE_LISTING_ENDPOINT,
)


class AdsAPI(BaseAPI):

    @staticmethod
    def _auth_headers(token: str) -> dict:
        return {"Authorization": f"Bearer {token}"}

    def create_ad(self, token: str, ad_data: dict):
        encoder = MultipartEncoder(fields=ad_data)
        headers = {
            **self._auth_headers(token),
            "Content-Type": encoder.content_type,
        }
        return self._request(
            "POST", CREATE_LISTING_ENDPOINT, data=encoder, headers=headers
        )

    def update_ad(self, token: str, ad_id: int, ad_data: dict):
        fields = dict(ad_data)
        fields["img1"] = "null"
        fields["img2"] = "null"
        fields["img3"] = "null"
        encoder = MultipartEncoder(fields=fields)
        headers = {
            **self._auth_headers(token),
            "Content-Type": encoder.content_type,
        }
        return self._request(
            "PATCH",
            UPDATE_OFFER_ENDPOINT.format(ad_id=ad_id),
            data=encoder,
            headers=headers,
        )

    def delete_ad(self, token: str, ad_id: int):
        return self._request(
            "DELETE",
            DELETE_LISTING_ENDPOINT.format(ad_id=ad_id),
            headers=self._auth_headers(token),
        )