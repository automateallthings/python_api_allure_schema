from tests.creds.creds import Creds
from utils.assertions.response_assertions import assert_status_code
from utils.headers import headers
from utils.logger import logger
from utils.request import APIRequest
from utils.url_builder import product_get_url

log = logger('product_client')


class ProductClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds

    def get_list_products_by_account_id(self, account_id):
        log.info('GET: Fetches list of the products associated to an account')
        response = self.request.get(product_get_url(account_id), headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = ProductClient(creds=creds)
