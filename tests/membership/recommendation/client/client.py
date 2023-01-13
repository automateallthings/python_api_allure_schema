import os

from config import GET_RECOMMENDATIONS_BY_ACCOUNT_ID, PUT_RECOMMENDATIONS_BY_ACCOUNT_ID
from tests.creds.creds import Creds
from tests.membership.recommendation.payload_builder.recommendation_payload_builder import \
    payload_add_recommendation_to_account
from utils.assertions.response_assertions import assert_status_code
from utils.logger import logger
from utils.request import APIRequest, headers

log = logger('recommendation_client')


class RecommendationClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds

    def get_recommendations_by_account_id(self, account_id):
        log.info('GET: Fetches list of the recommendations associated to an account')
        url = f'{os.getenv("BASE_URL")}{GET_RECOMMENDATIONS_BY_ACCOUNT_ID.replace("accountId", account_id)}'
        log.info('URL: ' + url)
        response = self.request.get(url, headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response

    def put_recommendations_to_account(self):
        log.info('PUT: Add recommendation to an account')
        url = f'{os.getenv("BASE_URL")}{PUT_RECOMMENDATIONS_BY_ACCOUNT_ID}'
        log.info('URL: ' + url)
        payload = payload_add_recommendation_to_account()
        response = self.request.put(url, payload, headers(self.creds.system_token))
        assert_status_code(response, 200)
        return response


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = RecommendationClient(creds=creds)
