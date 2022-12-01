from accounts import PASS_MEMBER_USER_ID
from clients.product_client import ProductClient
from tests.assertions.response_assertions import assert_status_code
from utils.authentication import employee_token
from utils.logger import logger

client = ProductClient()
log = logger('product_tests')


def test_get_products_for_pass_member():
    log.info('When: Member get a list of the products associated to an account')
    products = client.get_list_products_by_account_id(PASS_MEMBER_USER_ID, employee_token())
    log.info('Then: Correct status code should be return')
    assert_status_code(products, 200)
