import pytest

from tests.creds.creds import Creds
from tests.membership.agreement.client.client import AgreementClient


@pytest.fixture(scope="session")
def agreement_client():
    creds = Creds()
    client = AgreementClient(creds=creds)
    yield client
