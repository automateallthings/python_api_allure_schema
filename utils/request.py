import json
from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


def headers(token):
    return {
        'Authorization': token,
        'Content-Type': 'application/json'
    }


class APIRequest:
    def get(self, url, header):
        response = requests.get(url, headers=header)
        return self.__get_responses(response)

    def post(self, url, payload, header):
        json_pyload = json.dumps(payload)
        response = requests.post(url, data=json_pyload, headers=header)
        return self.__get_responses(response)

    def delete(self, url, header):
        response = requests.delete(url, headers=header)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        header = response.headers

        return Response(
            status_code, text, as_dict, header
        )
