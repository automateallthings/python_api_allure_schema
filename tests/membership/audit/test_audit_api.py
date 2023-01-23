import os

import pytest

from utils.assertions.soft_assert import soft_assert, verify_expectations
from utils.logger import logger

log = logger('audit_tests')


@pytest.mark.audit
@pytest.mark.regression
@pytest.mark.contract
def test_post_share_product_validate_response_status_code(audit_client):
    log.info('Given: Admin audit pass subscription for given account')
    response = audit_client.get_pass_subscription_audit_by_account_product_id_as_admin(
        os.getenv('AUDIT_ACCOUNT_PRODUCT_ID'))
    log.info('When: Correct filed and values is returned')
    soft_assert(response.as_dict[0]["dryFlyAccountProductId"] == os.getenv('AUDIT_ACCOUNT_PRODUCT_ID'))
    soft_assert(response.as_dict[0]["auditedBy"] == "pva@insp.com")
    soft_assert(response.as_dict[0]["data"]["accountId"] == 991000141)
    soft_assert(response.as_dict[0]["data"]["accountProductId"] == os.getenv('AUDIT_ACCOUNT_PRODUCT_ID'))
    soft_assert(response.as_dict[0]["data"]["accountUsers"][0]["dryFlyAccountUserId"] == 3910149)
    soft_assert(response.as_dict[0]["type"] == "Created")
    soft_assert(response.as_dict[1]["type"] == "Booking")
    soft_assert(response.as_dict[2]["type"] == "CancelBooking")
    soft_assert(response.as_dict[3]["type"] == "Updated")
    soft_assert(response.as_dict[4]["type"] == "Deleted")
    verify_expectations()
    log.info('Then: Response contain correct filed and values. Validation is passed')
