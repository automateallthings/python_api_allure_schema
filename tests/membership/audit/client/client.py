import os

from config import GET_PASS_SUBSCRIPTION_BY_ACCOUNT_PRODUCT_ID
from tests.creds.creds import Creds
from utils.assertions.response_assertions import assert_status_code
from utils.logger import logger
from utils.request import APIRequest, headers

log = logger('audit_client')


class AuditClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds


    def get_pass_subscription_audit_by_account_product_id_as_admin(self, account_product_id):
        url = f'{os.getenv("BASE_URL")}{GET_PASS_SUBSCRIPTION_BY_ACCOUNT_PRODUCT_ID.replace("accountProductId", account_product_id)}'
        log.info('URL: ' + url)
        response = self.request.get(url, headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = AuditClient(creds=creds)
