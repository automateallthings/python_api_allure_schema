from utils.json_formater import pretty_response
from utils.logger import logger

log = logger('response_assertions')


def assert_status_code(response, expected_status_code):
    if bool(response.text):
        response_body = "Response body: \n" + pretty_response(response.text)
        log.info(response_body)
    response_status_code = response.status_code
    if response_status_code == expected_status_code:
        log.info('Status code ' + str(expected_status_code) + ' as expected')
    else:
        log.error('Status code ' + str(response_status_code) + ' is not expected')
        raise Exception('Status code ' + str(response_status_code) + ' is not expected')
