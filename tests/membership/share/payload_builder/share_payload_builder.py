from utils.file_reader import read_payload_file
from utils.json_formater import pretty_payload
from utils.logger import logger

log = logger('share_payload_builder')


def payload_create_new_share(product_id, recipient_account_id):
    payload = read_payload_file('share_post_create_new_share.json', 'share')
    payload['ProductId'] = product_id
    payload['RecipientAccountId'] = recipient_account_id
    log.info('Payload: \n' + pretty_payload(payload))
    return payload
