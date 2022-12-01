import json

from utils.logger import logger

log = logger('response_assertions')


def assert_status_code(response, expected_status_code):
    json_object = json.loads(response.text)
    json_formatter = json.dumps(json_object, indent=2)
    response_body = "Response body: \n" + json_formatter
    response_status_code = response.status_code
    if response_status_code == expected_status_code:
        log.info('API call returns ' + str(expected_status_code) + ' as expected')
        log.info(response_body)
    else:
        log.error('API call returns ' + str(response_status_code) + ' is not expected')
        log.error(response_body)
        raise Exception(str(response_status_code) + ' is not expected')
