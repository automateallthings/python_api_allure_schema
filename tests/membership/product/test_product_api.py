import os

import pytest
from assertpy import assert_that

from tests.membership.product.client.product_client import ProductClient
from utils.authentication import employee_token
from utils.logger import logger

client = ProductClient()
log = logger('product_tests')


@pytest.mark.regression
@pytest.mark.contract
def test_get_products_for_pass_member_validate_response_status_code():
    log.info('Given: Member get a list of the products associated to an account')
    products = client.get_list_products_by_account_id(os.getenv('PASS_MEMBER_USER_ID'), employee_token())
    log.info('When: Correct status code should be return')
    assert_that(products.status_code == 200)
    log.info('Then: Status code passed validation')
