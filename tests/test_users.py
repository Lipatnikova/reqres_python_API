import logging
import pytest

from data.expected_result import ExpectedRequestsResult as Code
from data.endpoints import UrlAndEndPoints as EndPoint
from generator.generator import random_num_user
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsUsersEndPoint:

    def test_get_list_users_response_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, 'Response status code is incorrect'

    def test_get_list_users_schemas(self):
        get_list_users = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}', 'list_users.json')
        logger.info(get_list_users.json())
        assert get_list_users, 'API response is incorrect'

    def test_get_single_user_response_status_code(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}{random_num_user}')
        assert get_single_user.status_code == Code.STATUS_CODE_OK, 'Status code is incorrect'

    def test_get_single_user_not_found_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.SINGLE_USER}23')
        response_status = response.status_code
        assert response_status == Code.NOT_FOUND, 'Response status code is incorrect'

    def test_get_single_user_schemas(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2', 'single_user.json')
        logger.info(get_single_user.json())
        assert get_single_user, 'API response is incorrect'


class TestUnknownEndPoint:

    def test_get_list_resource_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, 'Response status code is incorrect'

    def test_get_single_resource_schemas(self):
        get_single_resource = HTTPHandler.get(f'{EndPoint.UNKNOWN}', 'list_resource.json')
        logger.info(get_single_resource.json())
        assert get_single_resource, 'API response is incorrect'

    def test_get_single_resource_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}{random_num_user()}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, 'Response status code is incorrect'

    def test_get_single_resource_not_found_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}/23')
        response_status = response.status_code
        assert response_status == Code.NOT_FOUND, 'Response status code is incorrect'

    @pytest.mark.xfail
    # Invalid JSON response schema is wrong?
    def test_get_single_random_id_resource_schemas(self):
        get_single_random_id_resource = HTTPHandler.get(f'{EndPoint.UNKNOWN}2',
                                                        'single_resource.json')
        logger.info(get_single_random_id_resource.json())
        assert get_single_random_id_resource, 'API response is incorrect'
