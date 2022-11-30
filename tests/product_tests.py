import requests

from assertpy import assert_that
from accounts import PASS_MEMBER_USER_ID
from utils.authentication import employee_token
from clients.product_client import ProductClient

client = ProductClient()


def test_get_products_for_pass_member():
    products = client.get_list_products_by_account_id(PASS_MEMBER_USER_ID, employee_token())

    assert_that(products.status_code, description='Incorrect response status code').is_equal_to(requests.codes.ok)
