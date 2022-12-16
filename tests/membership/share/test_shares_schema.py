import os

import pytest
from assertpy import assert_that

from utils.assertions.schema_assertions import schema_is_valid
from utils.logger import logger

log = logger('schema_tests')


@pytest.mark.shares
@pytest.mark.regression
@pytest.mark.contract
@pytest.mark.schema
def test_schema_fetches_shares_given_and_received(share_client):
    log.info('Given: Member fetches shares given and received')
    response = share_client.get_shares(os.getenv('GET_SHARE_ACCOUNT_ID'))
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'fetches_shares_given_and_received_for_account', 'share')).is_equal_to(True)
    log.info('Then: Schema passed validation')


@pytest.mark.shares
@pytest.mark.regression
@pytest.mark.contract
@pytest.mark.schema
def test_schema_create_new_share(share_client):
    log.info('Given: Member create a new share')
    response = share_client.post_create_new_share(os.getenv('SHARE_ACCOUNT_ID'), os.getenv('SHARE_PRODUCT_ID_SCHEMA'),
                                                  os.getenv('SHARE_RECIPIENT_ACCOUNT_ID'))
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'create_new_share_and_returns_share_id', 'share')).is_equal_to(True)
    log.info('Then: Schema passed validation')
