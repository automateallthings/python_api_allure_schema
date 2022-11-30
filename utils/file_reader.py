import json
import os

BASE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'data'))


def read_file(file_name):
    path = get_file_with_json_extension(file_name)
    with open(path) as f:
        return json.load(f)


def get_file_with_json_extension(file_name):
    if '.json' in file_name:
        path = os.path.join(BASE_PATH, file_name)
    else:
        path = os.path.join(BASE_PATH, f'{file_name}.json')
    return path
