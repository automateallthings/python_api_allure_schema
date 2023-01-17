import os

from config import GET_AGREEMENT_BY_ID
from tests.creds.creds import Creds
from utils.assertions.response_assertions import assert_status_code
from utils.logger import logger
from utils.request import APIRequest, headers

log = logger('agreement_client')


class AgreementClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds

    def get_agreement_by_id_as_admin(self, agreement_id):
        log.info('GET: Get agreement information by agreement id')
        url = f'{os.getenv("BASE_URL")}{GET_AGREEMENT_BY_ID.replace("agreementId", str(agreement_id))}'
        log.info('URL: ' + url)
        response = self.request.get(url, headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = AgreementClient(creds=creds)
