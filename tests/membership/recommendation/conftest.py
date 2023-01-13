import pytest

from tests.creds.creds import Creds
from tests.membership.recommendation.client.client import RecommendationClient


@pytest.fixture(scope="session")
def recommendation_client():
    creds = Creds()
    client = RecommendationClient(creds=creds)
    yield client
