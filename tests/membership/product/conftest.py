import pytest

from tests.creds.creds import Creds
from tests.domain.product.client.client import ProductClient


@pytest.fixture(scope="session")
def product_client():
    creds = Creds()
    client = ProductClient(creds=creds)
    yield client