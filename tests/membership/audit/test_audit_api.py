import os

import pytest
from assertpy import assert_that

from utils.logger import logger

log = logger('audit_tests')



@pytest.mark.audit
@pytest.mark.regression
@pytest.mark.contract
def test_post_share_product_validate_response_status_code(audit_client):
    log.info('Given: Admin audit pass subscription for given account')
    response = audit_client.get_pass_subscription_audit_by_account_product_id_as_admin(
        os.getenv('AUDIT_ACCOUNT_PRODUCT_ID'))
    log.info('When: Correct response schema is returned')