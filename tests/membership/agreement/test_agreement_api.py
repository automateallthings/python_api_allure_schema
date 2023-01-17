import pytest
from assertpy import assert_that

from utils.logger import logger

log = logger('agreement_tests')


@pytest.mark.agreement
@pytest.mark.regression
@pytest.mark.contract
def test_agreement_details_by_agreement_id(agreement_client):
    log.info('Given: Get agreement details by agreement ID')
    response = agreement_client.get_agreement_by_id_as_admin(1)
    log.info('When: Correct status code should be return')
    assert_that(response.status_code == 200)
    log.info('Then: Status code passed validation')
