from utils.file_reader import read_payload_file


def payload_create_new_share(product_id, recipient_account_id):
    payload = read_payload_file('share_post_create_new_share.json')
    payload['ProductId'] = product_id
    payload['RecipientAccountId'] = recipient_account_id
    return payload
