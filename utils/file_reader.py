import json
import os

SCHEMA_BASE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'data', 'schemas'))
PAYLOAD_BASE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'data', 'payloads'))


def read_schema_file(file_name):
    path = get_file_with_json_extension(SCHEMA_BASE_PATH, file_name)
    with open(path) as f:
        return json.load(f)


def read_payload_file(file_name):
    path = get_file_with_json_extension(PAYLOAD_BASE_PATH, file_name)
    with open(path) as f:
        return json.load(f)


def get_file_with_json_extension(file_path, file_name):
    if '.json' in file_name:
        path = os.path.join(file_path, file_name)
    else:
        path = os.path.join(file_path, f'{file_name}.json')
    return path
