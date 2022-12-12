import os

import pytest

from accounts import *


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test')


@pytest.fixture
def get_env(request):
    _env = request.config.getoption('--env')
    os.environ['ENVIRONMENT'] = _env
    return _env


@pytest.fixture(autouse=True)
def get_url(get_env):
    if get_env == 'test':
        _url = 'https://app-membershipapi-test.azurewebsites.net'
        os.environ['BASE_URL'] = _url
    elif get_env == 'qa':
        _url = 'https://app-membershipapi-qa.azurewebsites.net'
        os.environ['BASE_URL'] = _url
    elif get_env == 'test_rs':
        _url = 'https://apis.test.inspirato.com/membership/apex-beta'
        os.environ['BASE_URL'] = _url
    elif get_env == 'qa_rs':
        _url = 'https://apis.qa.inspirato.com/membership/apex-beta'
        os.environ['BASE_URL'] = _url

    if 'test' in str(get_env):
        os.environ['PASS_MEMBER_USER_ID'] = str(TEST_PASS_MEMBER_USER_ID)
        os.environ['SHARE_RECIPIENT_ACCOUNT_ID'] = str(TEST_SHARE_RECIPIENT_ACCOUNT_ID)
        os.environ['SHARE_PRODUCT_ID'] = str(TEST_SHARE_PRODUCT_ID)
        os.environ['SHARE_ACCOUNT_ID'] = str(TEST_SHARE_ACCOUNT_ID)
