from assertpy import assert_that

from accounts import PASS_MEMBER_USER_ID
from utils.authentication import employee_token
from clients.product_client import ProductClient
from tests.assertions.schema_assertions import schema_is_valid

client = ProductClient()


def test_get_products_for_pass_member():
    response = client.get_list_products_by_account_id(PASS_MEMBER_USER_ID, employee_token())

    assert_that(schema_is_valid(response.as_dict, 'product_associated_to_account')).is_equal_to(True)
