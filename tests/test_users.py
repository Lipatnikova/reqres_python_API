import logging
from data.expected_result import ExpectedRequestsResult as Code
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsUsersEndPoint:

    def test_get_list_users_response_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.LIST_USERS}2')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, 'Response status code is incorrect'

    def test_get_list_users_schemas(self):
        get_list_users = HTTPHandler.get(f'{EndPoint.LIST_USERS}2', 'list_users.json')
        logger.info(get_list_users.json())
        assert get_list_users, 'API response is incorrect'

    def test_get_single_user_response_status_code(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2')
        assert get_single_user.status_code == Code.STATUS_CODE_OK, 'Status code is incorrect'

    def test_get_single_user_schemas(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2', 'single_user.json')
        logger.info(get_single_user.json())
        assert get_single_user, 'API response is incorrect'
