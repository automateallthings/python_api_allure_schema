from utils.logger import logger

log = logger('response_assertions')


def validate_response_status_code(response, expected_status_code, description):
    response_body = "Response body: \n" + response.text
    response_status_code = response.status_code
    if response_status_code == expected_status_code:
        log.info(description + " returns " + str(expected_status_code) + " as expected")
        log.info(response_body)
    else:
        log.error(description + " returns " + str(response_status_code) + " is not expected")
        log.error(response_body)
        raise Exception(str(response_status_code) + " is not expected")
