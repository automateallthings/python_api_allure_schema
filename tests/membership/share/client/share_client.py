import os

from config import GET_POST_SHARE_BY_ACCOUNT_ID
from tests.membership.share.payload_builder.share_payload_builder import payload_create_new_share
from utils.assertions.response_assertions import assert_status_code
from utils.headers import headers
from utils.logger import logger
from utils.request import APIRequest

log = logger('share_client')


class ShareClient:
    def __init__(self):
        self.request = APIRequest()

    def post_create_new_share(self, account_id, product_id, recipient_account_id, token):
        log.info('Create a new share and returns created share id')
        BASE_URL = os.getenv('BASE_URL')
        url = f'{BASE_URL}{GET_POST_SHARE_BY_ACCOUNT_ID.replace("accountId", str(account_id))}'
        log.info('URL: ' + url)
        payload = payload_create_new_share(product_id, recipient_account_id)
        response = self.request.post(url, payload, headers(token))
        assert_status_code(response, 201)
        return response
