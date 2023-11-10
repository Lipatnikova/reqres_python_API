import logging

from data_tests.data_tests import DataPost, random_num_user, DataPut
from data_tests.expected_result import ExpectedRequestsResult as Code
from data_tests.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsUsersEndPoint:

    def test_get_list_users_response_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_get_list_users_schemas(self):
        get_list_users = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}', 'list_users.json')
        logger.info(get_list_users.json())
        assert get_list_users, logger.warning('API response is incorrect')

    def test_get_single_user_response_status_code(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2')
        assert get_single_user.status_code == Code.STATUS_CODE_OK, logger.warning('Status code is incorrect')

    def test_get_single_user_not_found_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.SINGLE_USER}23')
        response_status = response.status_code
        assert response_status == Code.NOT_FOUND, logger.warning('Response status code is incorrect')

    def test_get_single_user_schemas(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2', 'single_user.json')
        logger.info(get_single_user.json())
        assert get_single_user, logger.warning('API response is incorrect')

    def test_post_create_user_status_code(self):
        response = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataPost.data_post_user)
        response_status = response.status_code
        logger.info(response_status)
        assert response_status == Code.CREATED, logger.warning('Response status code is incorrect')

    def test_post_create_user_response_verify_schema(self):
        create_user = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataPost.data_post_user, 'create_user.json')
        logger.info(create_user.json())
        assert create_user, logger.warning('API response is incorrect')

    def test_put_create_and_update_user_status_code(self):
        response1 = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataPost.data_post_user)
        logger.info(response1)
        assert response1.status_code == Code.CREATED, logger.warning('Response status code is incorrect')
        response2 = HTTPHandler.put(f'{EndPoint.SINGLE_USER}2', DataPut.data_put_user)
        logger.info(response2)
        assert response2.status_code == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')
        assert response1 != response2, logger.warning("Response doesn't change")
