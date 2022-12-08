from assertpy import assert_that

from accounts import PASS_MEMBER_USER_ID
from clients.product_client import ProductClient
from tests.assertions.schema_assertions import schema_is_valid
from utils.authentication import employee_token
from utils.logger import logger

client = ProductClient()
log = logger('schema_tests')


def test_schema_get_products_for_pass_member():
    log.info('Given: Member get a list of the products associated to an account')
    response = client.get_list_products_by_account_id(PASS_MEMBER_USER_ID, employee_token())
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'product_products_associated_to_account')).is_equal_to(True)
    log.info('Then: Schema passed validation')
