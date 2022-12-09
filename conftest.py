import os

import pytest


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='test')


@pytest.fixture
def get_env(request):
    _base_url = request.config.getoption('--env')
    return _base_url


@pytest.fixture(autouse=True)
def get_url(get_env):
    if get_env == 'test':
        _url = 'https://app-membershipapi-test.azurewebsites.net'
        os.environ['BASE_URL'] = _url
    elif get_env == 'test2':
        _url = 'https://app-membershipapi-test2.azurewebsites.net'
        os.environ['BASE_URL'] = _url
    elif get_env == 'test6':
        _url = 'https://app-membershipapi-test6.azurewebsites.net'
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
