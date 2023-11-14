import logging

from data.expected_result import ExpectedText
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsLogoutEndPoint:

    def test_logout_verify_content_type(self):
        response = HTTPHandler.get(f'{EndPoint.LOGOUT}')
        logger.info(response.headers['Content-Type'])
        assert ExpectedText.content_type in response.headers['Content-Type'], \
            logger.warning('The headers Content-Type is wrong.')
