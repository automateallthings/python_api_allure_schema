import logging.config
import os


def logger(config):
    ini_path = os.path.join(os.path.dirname(__file__), '..', 'config_allure.ini')
    ini_file = os.path.realpath(ini_path)
    logging.config.fileConfig(ini_file)
    log = logging.getLogger(config)
    return log
