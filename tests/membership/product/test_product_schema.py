import os

import pytest
from assertpy import assert_that

from utils.assertions.schema_assertions import schema_is_valid
from utils.logger import logger

log = logger('schema_tests')


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.contract
@pytest.mark.schema
def test_schema_test_get_products_for_pass_member(product_client):
    log.info('Given: Member get a list of the products associated to an account')
    response = product_client.get_list_products_by_account_id(os.getenv('PASS_MEMBER_USER_ID'))
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'products_associated_to_account', 'product')).is_equal_to(True)
    log.info('Then: Schema passed validation')
