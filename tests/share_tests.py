from assertpy import assert_that

from accounts import SHARE_PRODUCT_ID, SHARE_ACCOUNT_ID, SHARE_RECIPIENT_ACCOUNT_ID
from clients.share_client import ShareClient
from utils.authentication import employee_token
from utils.logger import logger

client = ShareClient()
log = logger('share_tests')


def test_post_share_product():
    log.info('Given: Member share product with other member')
    products = client.post_create_new_share(SHARE_ACCOUNT_ID, SHARE_PRODUCT_ID, SHARE_RECIPIENT_ACCOUNT_ID,
                                            employee_token())
    log.info('When: Correct status code should be return')
    assert_that(products.status_code == 201)
    log.info('Then: Status code passed validation')
