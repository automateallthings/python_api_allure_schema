from config import BASE_URI, GET_LIST_PRODUCT_BY_ACCOUNT_ID
from utils.assertions.response_assertions import assert_status_code
from utils.headers import headers
from utils.logger import logger
from utils.request import APIRequest

log = logger('product_client')


class ProductClient:
    def __init__(self):
        self.request = APIRequest()

    def get_list_products_by_account_id(self, account_id, token):
        log.info('Get list of the products associated to an account')
        url = f'{BASE_URI}{GET_LIST_PRODUCT_BY_ACCOUNT_ID.replace("accountId", str(account_id))}'
        log.info("URL: " + url)
        response = self.request.get(url, headers(token))
        assert_status_code(response, 200)
        return response
