import os
import secrets
import string

from utils.file_reader import read_payload_file
from utils.json_formater import pretty_payload
from utils.logger import logger

log = logger('recommendation_payload_builder')


def payload_add_recommendation_to_account():
    """
    method to build recommendation payload to 1 account
    """
    payload = read_payload_file('add_recommendation_to_account.json', 'recommendation')
    _random_recommendation_asset_id()
    payload['recommendations'][0]['recommended_consolidated_asset_ids'][0] = os.getenv('ASSET_ID')
    log.info('Payload: \n' + pretty_payload(payload))
    return payload


def payload_add_recommendation_to_accounts():
    """
    Will be used later for future tests
    method to build recommendation payload for N accounts
    """
    payload = read_payload_file('add_recommendation_to_accounts.json', 'recommendation')
    _random_recommendation_asset_id()
    for i in range(len(payload['recommendations'])):
        payload['recommendations'][i]['recommended_consolidated_asset_ids'][0] = os.getenv('ASSET_ID')
    log.info('Payload: \n' + pretty_payload(payload))
    return payload


def _random_recommendation_asset_id():
    """
    method create random assetId for recommendation
    and save it as environment variable for future verification
    """
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(11))
    os.environ["ASSET_ID"] = str(res)
