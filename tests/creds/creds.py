import os

import requests
from assertpy import assert_that

AUTH_URL = 'https://test-signin.inspirato.com/oauth2/default/v1/token'


class Creds:
    """Class to store all credentials needed for auth at runtime."""

    def __init__(self):
        self._okta_username: str = os.getenv("OCTA_USERNAME")
        self._okta_password: str = os.getenv("PASSWORD")
        self._okta_token: str = ""

    @property
    def okta_token(self) -> str:
        """
        property to get the octa token
        """
        if not self._okta_token:
            self._get_okta_token()
        return self._okta_token

    def _get_okta_token(self):
        """
        Helper function to get okta token if it's not already set.
        """
        data = {
            'client_id': '0oa1lqmstdfm3KHeA0h8',
            'grant_type': 'password',
            'scope': 'membership.write membership.read',
            'username': self._okta_username,
            'password': self._okta_password
        }
        response = requests.post(AUTH_URL, data=data)
        assert_that(response.status_code, description='Employee token not created. Authentication failed') \
            .is_equal_to(requests.codes.ok)
        response_json = response.json()
        self._okta_token = 'Bearer ' + response_json['access_token']


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    print(token)
