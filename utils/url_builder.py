import os

from config import *
from utils.logger import logger

log = logger('url_builder')


# Account
# Agreement
# Audit
# DataImport
# Membership
# Product
def product_get_url(account_id):
    base_url = os.getenv('BASE_URL')
    url = f'{base_url}{GET_LIST_PRODUCT_BY_ACCOUNT_ID.replace("accountId", account_id)}'
    log.info('URL: ' + url)
    return url


# Recommendation
# Relationship
# Share
def share_get_post_url(account_id):
    base_url = os.getenv('BASE_URL')
    url = f'{base_url}{GET_POST_SHARE_BY_ACCOUNT_ID.replace("accountId", account_id)}'
    log.info('URL: ' + url)
    return url


def share_delete_url(account_id, share_id):
    base_url = os.getenv('BASE_URL')
    url = f'{base_url}{DELETE_SHARE_BY_ACCOUNT_ID_SHARE_ID.replace("accountId", account_id).replace("shareId", share_id)}'
    log.info('URL: ' + url)
    return url
