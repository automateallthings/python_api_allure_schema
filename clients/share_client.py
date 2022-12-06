from config import BASE_URI, GET_POST_SHARE_BY_ACCOUNT_ID
from tests.assertions.response_assertions import assert_status_code
from utils.headers import headers
from utils.json_formater import pretty_payload
from utils.logger import logger
from utils.request import APIRequest

log = logger('share_client')


class ShareClient:
    def __init__(self):
        self.request = APIRequest()

    def post_create_new_share(self, account_id, product_id, recipient_account_id, token):
        payload = {
            "ProductId": product_id,
            "RecipientAccountId": recipient_account_id,
            "StartDate": "2022-12-06T17:54:28.981Z",
            "EndDate": "2022-12-06T17:54:28.981Z",
            "MinCost": 1000,
            "MaxCost": 10000,
            "UsageQuantity": 1,
            "PersonalMessage": "Hey! This is for you"
        }
        log.info('Create a new share and returns created share id')
        url = f'{BASE_URI}{GET_POST_SHARE_BY_ACCOUNT_ID.replace("accountId", str(account_id))}'
        log.info('URL: ' + url)
        log.info('Payload: \n' + pretty_payload(payload))
        response = self.request.post(url, payload, headers(token))
        assert_status_code(response, 201)
        return response
