import logging
import pytest

from data.expected_result import ExpectedRequestsResult as Code
from data.endpoints import UrlAndEndPoints as EndPoint
from data.expected_result import ExpectedText
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestUnknownEndPoint:

    def test_get_list_resource_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_get_single_resource_schemas(self):
        get_single_resource = HTTPHandler.get(f'{EndPoint.UNKNOWN}', 'list_resource.json')
        logger.info(get_single_resource.json())
        assert get_single_resource, logger.warning('API response is incorrect')

    def test_get_single_resource_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}/2')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_get_single_resource_not_found_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}/23')
        response_status = response.status_code
        assert response_status == Code.NOT_FOUND, logger.warning('Response status code is incorrect')

    def test_get_single_random_id_resource_schemas(self):
        get_single_random_id_resource = HTTPHandler.get(f'{EndPoint.UNKNOWN}/2',
                                                        'single_resource.json')
        logger.info(get_single_random_id_resource.json())
        assert get_single_random_id_resource, logger.warning('API response is incorrect')

    def test_get_list_resource_verify_content_type(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}')
        logger.info(response.headers['Content-Type'])
        assert ExpectedText.content_type in response.headers['Content-Type'], \
            logger.warning('The headers Content-Type is wrong.')

    def test_get_list_resource_response_count_headers(self):
        response = HTTPHandler.get(f'{EndPoint.UNKNOWN}')
        headers = len(response.headers)
        print(*response.headers.keys(), sep='; ')
        assert headers == 18, logger.warning('Count of headers is not correct')
