import os

import pytest
from assertpy import assert_that

from tests.membership.share.client.share_client import ShareClient
from utils.authentication import employee_token
from utils.logger import logger

client = ShareClient()
log = logger('share_tests')


# TODO Finished after the MEM-399 will be done
@pytest.fixture()
def enroll_new_member():
    # 1 Enroll new member. Products: select, select trip bundle, select booking
    # 2 Retrieve member's product -
    # 3 Search for AccountProductId of Inspirato Select Booking (ProductID = 325), return AccountProductId
    # 4 Pass this value to test_post_share_product_validate_response_status_code()
    pass


@pytest.mark.regression
@pytest.mark.contract
def test_post_share_product_validate_response_status_code(enroll_new_member):
    log.info('Given: Member share product with other member')
    products = client.post_create_new_share(os.getenv('SHARE_ACCOUNT_ID'), os.getenv('SHARE_PRODUCT_ID'),
                                            os.getenv('SHARE_RECIPIENT_ACCOUNT_ID'),
                                            employee_token())
    log.info('When: Correct status code should be return')
    assert_that(products.status_code == 201)
    log.info('Then: Status code passed validation')
