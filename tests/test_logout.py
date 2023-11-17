import logging

from data.data import DataLoginUser
from data.expected_result import ExpectedText, ExpectedRequestsResult
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsLogoutEndPoint:

    def test_logout_after_login_status_code(self):
        response1 = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        logger.info(response1.json())
        response2 = HTTPHandler.post(f'{EndPoint.LOGOUT}', {})
        response_status = response2.status_code
        logger.info(response_status)
        assert response_status == ExpectedRequestsResult.STATUS_CODE_OK, \
            logger.warning('Response status code is incorrect')

    def test_logout_after_login_verify_count_response_headers(self):
        response1 = HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        logger.info(response1.json())
        response2 = HTTPHandler.post(f'{EndPoint.LOGOUT}', {})
        headers = len(response2.headers.keys())
        logger.info(headers)
        assert 14 == headers, logger.warning('Count of headers is not correct')

    def test_logout_verify_content_type(self):
        response = HTTPHandler.get(f'{EndPoint.LOGOUT}')
        logger.info(response.headers['Content-Type'])
        assert ExpectedText.content_type in response.headers['Content-Type'], \
            logger.warning('The headers Content-Type is wrong.')

    def test_logout_time_elapsed_between_sending_the_request_and_the_arrival_of_the_response(self):
        HTTPHandler.post(f'{EndPoint.LOGIN}', DataLoginUser.data_login)
        response = HTTPHandler.post(f'{EndPoint.LOGOUT}', {})
        time_elapsed = int(str(response.elapsed).split('.', 5)[1])
        logger.info(response.elapsed)
        assert time_elapsed <= 500000, f'Time elapsed between sending the request and ' \
                                       f'the arrival of the response: 0:00:00.{time_elapsed}'
