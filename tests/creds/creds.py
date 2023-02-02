import os
from base64 import b64encode

import requests
from assertpy import assert_that

AUTH_URL = 'https://test-signin.inspirato.com/oauth2/default/v1/token'


class Creds:
    """Class to store all credentials needed for auth at runtime."""

    def __init__(self):
        self._okta_username: str = os.getenv("OKTA_USERNAME")
        self._okta_password: str = os.getenv("OKTA_PASSWORD")
        self._okta_token: str = ""
        self._system_username: str = os.getenv("SYSTEM_USERNAME")
        self._system_password: str = os.getenv("SYSTEM_PASSWORD")
        self._system_token: str = ""
        self._client_id: str = os.getenv("CLIENT_ID")

    @property
    def okta_token(self) -> str:
        """
        property to get the okta token
        """
        if not self._okta_token:
            self._get_okta_token()
        return self._okta_token

    @property
    def system_token(self) -> str:
        """
        property to get the system token
        """
        if not self._system_token:
            self._get_system_token()
        return self._system_token

    def _get_okta_token(self):
        """
        Helper function to get okta token if it's not already set.
        """
        data = {
            'client_id': self._client_id,
            'grant_type': 'password',
            'scope': 'domain.write domain.read',
            'username': self._okta_username,
            'password': self._okta_password
        }
        response = requests.post(AUTH_URL, data=data)
        assert_that(response.status_code, description='Employee token not created. Authentication failed') \
            .is_equal_to(requests.codes.ok)
        response_json = response.json()
        self._okta_token = 'Bearer ' + response_json['access_token']

    def _get_system_token(self):
        """
        Set up the system token.
        """
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self._basic_auth(self._system_username, self._system_password),
        }

        data = {
            'grant_type': 'client_credentials',
            'scope': 'domain.write',
        }
        response = requests.post(AUTH_URL, headers=header, data=data)
        assert_that(response.status_code, description='System token not created. Authentication failed') \
            .is_equal_to(requests.codes.ok)
        response_json = response.json()
        self._system_token = 'Bearer ' + response_json['access_token']

    @staticmethod
    def _basic_auth(username, password):
        base_auth = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
        return f'Basic {base_auth}'


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    print(token)
