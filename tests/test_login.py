import logging

from data.data import DataLoginUser
from data.expected_result import ExpectedRequestsResult as Code
from data.expected_result import ExpectedMessage as Msg
from data.expected_result import ExpectedText
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

    def test_login_successful_response_count_headers(self):
        response = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        headers = len(response.headers)
        assert headers == 14, logger.warning('Count of headers is not correct')

    def test_login_successful_verify_content_type(self):
        response = HTTPHandler.get(f'{EndPoint.LOGIN}')
        logger.info(response.headers['Content-Type'])
        assert ExpectedText.content_type in response.headers['Content-Type'], \
            logger.warning('The headers Content-Type is wrong.')

    def test_login_time_elapsed_between_sending_the_request_and_the_arrival_of_the_response(self):
        response = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        time_elapsed = int(str(response.elapsed).split('.', 5)[1])
        logger.info(response.elapsed)
        assert time_elapsed <= 500000, f'Time elapsed between sending the request and ' \
                                       f'the arrival of the response: 0:00:00.{time_elapsed}'

