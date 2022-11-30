import requests
from config import AUTH_URL
from accounts import EMPLOYEE_USER, PASSWORD
from assertpy import assert_that


def employee_token():
    data = {
        'client_id': '0oa1lqmstdfm3KHeA0h8',
        'grant_type': 'password',
        'scope': 'membership.write membership.read',
        'username': EMPLOYEE_USER,
        'password': PASSWORD
    }
    response = requests.post(AUTH_URL, data=data)
    assert_that(response.status_code, description='Employee token not created. Authentication failed')\
        .is_equal_to(requests.codes.ok)
    response_json = response.json()
    return 'Bearer ' + response_json['access_token']


def member_token(username):
    data = {
        'client_id': '0oa1lqmstdfm3KHeA0h8',
        'grant_type': 'password',
        'scope': 'membership.write membership.read',
        'username': username,
        'password': PASSWORD
    }
    response = requests.post(AUTH_URL, data=data)
    assert_that(response.status_code, description='Member token not created. Authentication failed')\
        .is_equal_to(requests.codes.ok)
    response_json = response.json()
    return 'Bearer ' + response_json['access_token']
