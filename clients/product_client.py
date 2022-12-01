from config import BASE_URI, GET_LIST_PRODUCT_BY_ACCOUNT_ID
from tests.assertions.response_assertions import validate_response_status_code
from utils.headers import headers
from utils.request import APIRequest


class ProductClient:
    def __init__(self):
        self.request = APIRequest()

    def get_list_products_by_account_id(self, account_id, token):
        url = f'{BASE_URI}{GET_LIST_PRODUCT_BY_ACCOUNT_ID.replace("accountId", account_id)}'

        response = self.request.get(url, headers(token))
        validate_response_status_code(response, 200, "List of products for account")
        return response
