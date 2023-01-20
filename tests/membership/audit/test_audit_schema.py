import os

import pytest
from assertpy import assert_that

from utils.assertions.schema_assertions import schema_is_valid
from utils.logger import logger

log = logger('schema_tests')


@pytest.mark.audit
@pytest.mark.regression
@pytest.mark.contract
def test_schema_pass_subscription_audit_as_admin(audit_client):
    log.info('Given: Admin audit pass subscription for given account')
    response = audit_client.get_pass_subscription_audit_by_account_product_id_as_admin(
        os.getenv('AUDIT_ACCOUNT_PRODUCT_ID'))
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'pass_subscription_audit', 'audit')).is_equal_to(True)
    log.info('Then: Schema passed validation')
