import pytest

from tests.creds.creds import Creds
from tests.membership.audit.client.client import AuditClient


@pytest.fixture(scope="session")
def audit_client():
    creds = Creds()
    client = AuditClient(creds=creds)
    yield client
