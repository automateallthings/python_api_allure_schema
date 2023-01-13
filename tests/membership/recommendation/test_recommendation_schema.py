import os

import pytest
from assertpy import assert_that

from utils.assertions.schema_assertions import schema_is_valid
from utils.logger import logger

log = logger('schema_tests')


@pytest.mark.recommendation
@pytest.mark.regression
@pytest.mark.contract
def test_add_recommendation_to_account(recommendation_client):
    log.info('Given: System admin add recommendation to an account')
    response = recommendation_client.put_recommendations_to_account()
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'put_recommendation_to_account', 'recommendation')).is_equal_to(True)
    log.info('Then: Schema passed validation')


@pytest.mark.recommendation
@pytest.mark.regression
@pytest.mark.contract
def test_get_recommendation_for_account(recommendation_client):
    log.info('Given: Member fetches recommendation associated to an account')
    response = recommendation_client.get_recommendations_by_account_id(os.getenv('REC_ACCOUNT_USER_ID_1'))
    log.info('When: Correct response schema is returned')
    assert_that(schema_is_valid(response, 'get_recommendation_for_account', 'recommendation')).is_equal_to(True)
    log.info('Then: Schema passed validation')
