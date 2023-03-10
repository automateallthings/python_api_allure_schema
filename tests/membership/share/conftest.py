import pytest

from tests.creds.creds import Creds
from tests.domain.share.client.client import ShareClient


@pytest.fixture(scope="session")
def share_client():
    creds = Creds()
    client = ShareClient(creds=creds)
    yield client
