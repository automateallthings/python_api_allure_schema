import os

from config import GET_LIST_PRODUCT_BY_ACCOUNT_ID
from tests.creds.creds import Creds
from utils.assertions.response_assertions import assert_status_code
from utils.logger import logger
from utils.request import APIRequest, headers

log = logger('product_client')


class ProductClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds

    def get_list_products_by_account_id(self, account_id):
        log.info('GET: Fetches list of the products associated to an account')
        url = f'{os.getenv("BASE_URL")}{GET_LIST_PRODUCT_BY_ACCOUNT_ID.replace("accountId", account_id)}'
        log.info('URL: ' + url)
        response = self.request.get(url, headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = ProductClient(creds=creds)
