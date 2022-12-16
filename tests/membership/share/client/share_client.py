import json
import os

from tests.creds.creds import Creds
from tests.membership.share.payload_builder.share_payload_builder import payload_create_new_share
from utils.assertions.response_assertions import assert_status_code
from utils.headers import headers
from utils.logger import logger
from utils.request import APIRequest
from utils.url_builder import share_get_post_url, share_delete_url

log = logger('share_client')


class ShareClient:
    def __init__(self, creds: Creds):
        self.request = APIRequest()
        self.creds = creds

    def post_create_new_share(self, account_id, product_id, recipient_account_id):
        log.info('POST: Create a new share')
        payload = payload_create_new_share(product_id, recipient_account_id)
        response = self.request.post(share_get_post_url(account_id), payload, headers(self.creds.okta_token))
        assert_status_code(response, 201)
        self._set_share_id(response)
        self._clear_share(account_id, os.environ.get("SHARE_ID"), product_id)
        return response

    def get_shares(self, account_id):
        log.info('GET: Fetches shares for given accountId')
        response = self.request.get(share_get_post_url(account_id), headers(self.creds.okta_token))
        assert_status_code(response, 200)
        return response

    def delete_share(self, account_id, product_id, recipient_account_id):
        self._create_share(account_id, product_id, recipient_account_id)
        log.info('DELETE: Delete a share for a given account id and share id')
        response = self.request.delete(share_delete_url(account_id, os.environ.get("SHARE_ID")),
                                       headers(self.creds.okta_token))
        assert_status_code(response, 204)
        return response

    @staticmethod
    def _set_share_id(response):
        body = json.loads(response.text)
        os.environ['SHARE_ID'] = str(body['id'])
        log.info('Set share id as environment variable. Share id ' + os.environ.get("SHARE_ID"))

    def _clear_share(self, account_id, share_id, product_id):
        log.info('Post condition: Delete a share for account id ' + account_id + ' and share id ' + share_id)
        response = self.request.delete(share_delete_url(account_id, share_id), headers(self.creds.okta_token))
        assert_status_code(response, 204)
        log.info('Post condition: Share id ' + share_id + ' deleted successfully')
        log.info('Post condition: Product Id  ' + product_id + ' can be reused again')

    def _create_share(self, account_id, product_id, recipient_account_id):
        log.info('Pre condition: Create a share for account id ' + account_id + ' and product id ' + product_id)
        payload = payload_create_new_share(product_id, recipient_account_id)
        response = self.request.post(share_get_post_url(account_id), payload, headers(self.creds.okta_token))
        assert_status_code(response, 201)
        self._set_share_id(response)
        log.info('Pre condition: Share created')


if __name__ == "__main__":
    creds = Creds()
    token = creds.okta_token
    client = ShareClient(creds=creds)
