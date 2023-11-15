import logging
import time
from datetime import datetime

from data.data import DataCreateUser, random_num_user, DataUpdateUser
from data.expected_result import ExpectedRequestsResult as Code
from data.endpoints import UrlAndEndPoints as EndPoint
from utils.http_handler import HTTPHandler

logger = logging.getLogger("api")


class TestsUsersEndPoint:

    def test_get_list_users_response_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_get_list_users_schema_json(self):
        verify_schema = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}', 'list_users.json')
        logger.info(verify_schema.json())
        assert verify_schema, logger.warning('API response is incorrect, wrong schema!')

    def test_get_list_users_response_count_headers(self):
        response = HTTPHandler.get(f'{EndPoint.LIST_USERS}{random_num_user}')
        headers = len(response.headers)
        assert headers == 17, logger.warning('Count of headers is not correct')

    def test_get_single_user_response_status_code(self):
        get_single_user = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2')
        assert get_single_user.status_code == Code.STATUS_CODE_OK, logger.warning('Status code is incorrect')

    def test_get_single_user_not_found_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.SINGLE_USER}23')
        response_status = response.status_code
        assert response_status == Code.NOT_FOUND, logger.warning('Response status code is incorrect')

    def test_get_single_user_schema_json(self):
        verify_schema = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2', 'single_user.json')
        logger.info(verify_schema.json())
        assert verify_schema, logger.warning('API response is incorrect, wrong schema')

    def test_get_single_user_response_count_headers(self):
        response = HTTPHandler.get(f'{EndPoint.SINGLE_USER}2')
        headers = len(response.headers)
        print(*response.headers.keys())
        assert headers == 17, logger.warning('Count of headers is not correct')

    def test_post_create_user_status_code(self):
        response = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataCreateUser.data_create_user)
        response_status = response.status_code
        logger.info(response_status)
        assert response_status == Code.CREATED, logger.warning('Response status code is incorrect')

    def test_post_create_user_response_verify_schema_json(self):
        verify_schema = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataCreateUser.data_create_user, 'create_user.json')
        logger.info(verify_schema.json())
        assert verify_schema, logger.warning('API response is incorrect, wrong schema')

    def test_post_create_user_response_verify_key_name(self):
        data = DataCreateUser.data_create_user
        logger.info(data['name'])
        create_user = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', data)
        logger.info(create_user.json()['name'])
        assert data['name'] == create_user.json()['name'], logger.warning('API response is incorrect')

    def test_post_create_user_response_verify_key_job(self):
        data = DataCreateUser.data_create_user
        logger.info(data['job'])
        create_user = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', data)
        logger.info(create_user.json()['job'])
        assert data['job'] == create_user.json()['job'], logger.warning('API response is incorrect')

    def test_put_create_and_update_user_status_code(self):
        response1 = HTTPHandler.post(f'{EndPoint.SINGLE_USER}', DataCreateUser.data_create_user)
        logger.info(response1)
        assert response1.status_code == Code.CREATED, logger.warning('Response status code is incorrect')
        response2 = HTTPHandler.put(f'{EndPoint.SINGLE_USER}2', DataUpdateUser.data_update_user)
        logger.info(response2)
        assert response2.status_code == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')
        assert response1 != response2, logger.warning("Response doesn't change")

    def test_put_update_user_verify_schema_json(self):
        verify_schema = HTTPHandler.put(f'{EndPoint.SINGLE_USER}2', DataUpdateUser.data_update_user, 'update_user.json')
        logger.info(verify_schema.json())
        assert verify_schema, logger.warning('API response is incorrect, wrong schema')

    def test_put_update_user_verify_key_updated_at(self):
        data = DataUpdateUser.data_update_user
        response = HTTPHandler.put(f'{EndPoint.SINGLE_USER}2', data).json()
        logger.info(response)
        today = str(datetime.today())[:10]
        assert today in response['updatedAt'], logger.warning('API response is incorrect')

    def test_patch_update_user_verify_key_updated_at(self):
        data = DataUpdateUser.data_update_user
        response = HTTPHandler.patch(f'{EndPoint.SINGLE_USER}2', data).json()
        logger.info(response)
        today = str(datetime.today())[:10]
        assert today in response['updatedAt'], logger.warning('API response is incorrect')

    def test_delete_user_status_code(self):
        response = HTTPHandler.delete(f'{EndPoint.SINGLE_USER}2')
        logger.info(response)
        assert response.status_code == Code.NO_CONTENT, logger.warning('Response status code is incorrect')

    def test_delete_user_content_after(self):
        response = HTTPHandler.delete(f'{EndPoint.SINGLE_USER}2')
        logger.info(response)
        assert response.text == '', logger.warning('Response contains content')

    def test_get_delay_list_users_response_status_code(self):
        response = HTTPHandler.get(f'{EndPoint.DELAY}3')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_get_delay_users_schema_json(self):
        start_time = time.time()
        verify_schema = HTTPHandler.get(f'{EndPoint.DELAY}3', 'list_users.json')
        end_time = time.time()
        delay = end_time - start_time
        logger.info(verify_schema.json())
        assert verify_schema, logger.warning('API response is incorrect, wrong schema')
        logger.info(delay)
        assert 3 <= delay, logger.warning('The delay time is wrong')
