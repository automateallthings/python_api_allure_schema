from config import BASE_URI, GET_LIST_PRODUCT_BY_ACCOUNT_ID
from utils.request import APIRequest
from utils.headers import headers


class ProductClient:
    def __init__(self):
        self.request = APIRequest()

    def get_list_products_by_account_id(self, account_id, token):
        url = f'{BASE_URI}{GET_LIST_PRODUCT_BY_ACCOUNT_ID.replace("accountId", account_id)}'
        response = self.request.get(url, headers(token))
        return response

