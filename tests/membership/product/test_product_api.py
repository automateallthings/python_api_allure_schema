import os

import pytest
from assertpy import assert_that

from utils.logger import logger

log = logger('product_tests')


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.contract
def test_get_products_for_pass_member_validate_response_status_code(product_client):
    log.info('Given: Member get a list of the products associated to an account')
    products = product_client.get_list_products_by_account_id(os.getenv('PASS_MEMBER_USER_ID'))
    log.info('When: Correct status code should be return')
    assert_that(products.status_code == 200)
    log.info('Then: Status code passed validation')
