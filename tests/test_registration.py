from data.email_generator import generate_email
from data.test_data import DEFAULT_PASSWORD, MSG_EMAIL_USED


class TestRegistration:

    def test_register_new_user_success(self, auth_api):
        email = generate_email()
        response = auth_api.signup(email, DEFAULT_PASSWORD)

        assert response.status_code == 201
        body = response.json()
        assert body["user"]["email"] == email
        assert "access_token" in body

    def test_register_existing_user_fails(self, auth_api):
        email = generate_email()
        auth_api.signup(email, DEFAULT_PASSWORD)

        response = auth_api.signup(email, DEFAULT_PASSWORD)

        assert response.status_code == 400
        body = response.json()
        assert body["statusCode"] == 400
        assert body["message"] == MSG_EMAIL_USED