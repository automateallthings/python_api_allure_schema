from utils.logger import logger

log = logger('response_assertions')


def test_one():
    log.info("Tom " + str(200))
    log.info("Tom " + str(201))
    log.info("Tom " + str(202))
