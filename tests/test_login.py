import logging

from data.data import DataLoginUser
from data.expected_result import ExpectedRequestsResult as Code
from data.expected_result import ExpectedMessage as Msg
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestLoginEndPoint:

    def test_login_successful_status_code(self):
        response = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        response_status = response.status_code
        logger.info(response_status)
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_login_successful_token(self):
        response = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        logger.info(response)
        assert response.json()['token'] == "QpwL5tke4Pnpja7X4"

    def test_login_wrong_email_verify_message(self):
        response = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login_wrong_email).json()
        logger.info(response)
        assert response == Msg.msg_not_password, logger.warning("Message 'Missing password' is wrong")
