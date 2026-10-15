from data.email_generator import generate_email
from data.test_data import DEFAULT_PASSWORD, MSG_INVALID_CREDENTIALS


class TestAuthorization:

    def test_login_registered_user_success(self, auth_api):
        email = generate_email()
        auth_api.signup(email, DEFAULT_PASSWORD)

        response = auth_api.signin(email, DEFAULT_PASSWORD)

        assert response.status_code == 201
        body = response.json()
        assert body["user"]["email"] == email
        assert "access_token" in body["token"]

    def test_login_nonexistent_email_fails(self, auth_api):
        response = auth_api.signin(generate_email(), DEFAULT_PASSWORD)

        assert response.status_code == 404
        body = response.json()
        assert body["statusCode"] == 404
        assert body["message"] == MSG_INVALID_CREDENTIALS

    def test_login_wrong_password_fails(self, auth_api):
        email = generate_email()
        auth_api.signup(email, DEFAULT_PASSWORD)

        response = auth_api.signin(email, "wrong_password")

        assert response.status_code == 404
        body = response.json()
        assert body["statusCode"] == 404
        assert body["message"] == MSG_INVALID_CREDENTIALS