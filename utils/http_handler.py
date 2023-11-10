import requests
import json
from utils.validator import validator
import os

from data_tests.endpoints import UrlAndEndPoints as EndPoint


class HTTPHandler:

    @staticmethod
    def validate_response(response, schemas):
        try:
            response_json = response.json()
            is_valid = validator(response_json, schemas)
            if not is_valid:
                raise Exception("Invalid JSON response")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response:", json.JSONDecodeError)

    @classmethod
    def get(cls, endpoint, schemas=None):
        url = f"{EndPoint.BASE_URL}{endpoint}"
        response = requests.get(url)
        if schemas:
            schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
            absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
            cls.validate_response(response, absolute_schemas_path_and_name)
        return response

    @classmethod
    def post(cls, endpoint, data, schemas=None):
        url = f"{EndPoint.BASE_URL}{endpoint}"
        response = requests.post(url, json=data)
        if schemas:
            schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
            absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
            cls.validate_response(response, absolute_schemas_path_and_name)
        return response

    @classmethod
    def put(cls, endpoint, data, schemas=None):
        url = f"{EndPoint.BASE_URL}{endpoint}"
        response = requests.put(url, json=data)
        if schemas:
            schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
            absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
            cls.validate_response(response, absolute_schemas_path_and_name)
        return response

    @classmethod
    def patch(cls, endpoint, data, schemas=None):
        url = f"{EndPoint.BASE_URL}{endpoint}"
        response = requests.patch(url, json=data)
        if schemas:
            schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
            absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
            cls.validate_response(response, absolute_schemas_path_and_name)
        return response

    @classmethod
    def delete(cls, endpoint, schemas=None):
        url = f"{EndPoint.BASE_URL}{endpoint}"
        response = requests.delete(url)
        if schemas:
            print('No schemas needed')
        return response
