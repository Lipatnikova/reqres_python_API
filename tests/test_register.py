import logging

from data.data import DataRegisterUser
from data.expected_result import ExpectedRequestsResult as Code
from data.expected_result import ExpectedMessage as Msg
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsRegisterEndPoint:

    def test_post_register_user_successful_status_code(self):
        data = DataRegisterUser.data_register_user
        response = HTTPHandler.post(f'{EndPoint.REGISTER}', data)
        response_status = response.status_code
        logger.info(response_status)
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_post_register_user_with_wrong_email(self):
        data = DataRegisterUser.data_register_user_wrong
        response = HTTPHandler.post(f'{EndPoint.REGISTER}', data)
        response_status = response.status_code
        logger.info(response_status)
        assert response_status == Code.BAD_REQUEST, logger.warning('Response status code is incorrect')

    def test_post_register_with_wrong_email_without_password_verify_message(self):
        data = DataRegisterUser.data_register_user_wrong
        response = HTTPHandler.post(f'{EndPoint.REGISTER}', data).json()
        logger.info(response)
        assert response == Msg.msg_not_password, logger.warning("Message 'Missing password' is wrong")

    def test_post_register_with_wrong_email_with_password_verify_message(self):
        data = DataRegisterUser.data_register_user_wrong_v2
        response = HTTPHandler.post(f'{EndPoint.REGISTER}', data).json()
        logger.info(response)
        assert response == Msg.msg_about_defined_users, logger.warning("Message is wrong")
