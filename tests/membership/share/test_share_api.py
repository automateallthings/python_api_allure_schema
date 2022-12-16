import os

import pytest
from assertpy import assert_that

from utils.logger import logger

log = logger('share_tests')


@pytest.mark.shares
@pytest.mark.regression
@pytest.mark.contract
def test_post_share_product_validate_response_status_code(share_client):
    log.info('Given: Member share product with other member')
    response = share_client.post_create_new_share(os.getenv('SHARE_ACCOUNT_ID'), os.getenv('SHARE_PRODUCT_ID_ADD'),
                                                  os.getenv('SHARE_RECIPIENT_ACCOUNT_ID'))
    log.info('When: Correct status code should be return')
    assert_that(response.status_code == 201)
    log.info('Then: Status code passed validation. Status code: ' + str(response.status_code))


@pytest.mark.shares
@pytest.mark.regression
@pytest.mark.contract
def test_get_shares_validate_response_status_code(share_client):
    log.info('Given: Member fetches shares given and received')
    response = share_client.get_shares(os.getenv('GET_SHARE_ACCOUNT_ID'))
    log.info('When: Correct status code should be return')
    assert_that(response.status_code == 200)
    log.info('Then: Status code passed validation. Status code: ' + str(response.status_code))


@pytest.mark.shares
@pytest.mark.regression
@pytest.mark.contract
def test_delete_share_validate_response_status_code(share_client):
    log.info('Given: Member delete a share for given account id and share id')
    response = share_client.delete_share(os.getenv('SHARE_ACCOUNT_ID'), os.getenv('SHARE_PRODUCT_ID_DELETE'),
                                         os.getenv('SHARE_RECIPIENT_ACCOUNT_ID'))
    log.info('When: Correct status code should be return')
    assert_that(response.status_code == 204)
    log.info('Then: Status code passed validation. Status code: ' + str(response.status_code))
