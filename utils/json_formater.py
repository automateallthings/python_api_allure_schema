import json


def pretty_response(response):
    json_object = json.loads(response)
    json_formatter = json.dumps(json_object, indent=4)
    return json_formatter


def pretty_payload(payload):
    json_formatter = json.dumps(payload, indent=4)
    return json_formatter
