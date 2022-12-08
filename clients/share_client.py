from config import BASE_URI, GET_POST_SHARE_BY_ACCOUNT_ID
from tests.assertions.response_assertions import assert_status_code
from tests.payload_builder.share_payload_builder import payload_create_new_share
from utils.headers import headers
from utils.json_formater import pretty_payload
from utils.logger import logger
from utils.request import APIRequest

log = logger('share_client')


class ShareClient:
    def __init__(self):
        self.request = APIRequest()

    def post_create_new_share(self, account_id, product_id, recipient_account_id, token):
        payload = payload_create_new_share(product_id, recipient_account_id)
        log.info('Create a new share and returns created share id')
        url = f'{BASE_URI}{GET_POST_SHARE_BY_ACCOUNT_ID.replace("accountId", str(account_id))}'
        log.info('URL: ' + url)
        log.info('Payload: \n' + pretty_payload(payload))
        response = self.request.post(url, payload, headers(token))
        assert_status_code(response, 201)
        return response
