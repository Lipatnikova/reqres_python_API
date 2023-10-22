import requests
import time


BASE_URL = 'https://reqres.in/'
GET_LIST_USERS = 'api/users?page='
SINGLE_USER = '/api/users'
SINGLE_USER_NOT_FOUND = 'api/users/23'
CREATE = 'api/users'


class TestsListUsers:
    def test_get_list_users_response_verify_second_page(self):
        url = f"{BASE_URL}{GET_LIST_USERS}2"
        response = requests.get(url)
        print('\n', response.json())
        assert response.json()['page'] == 2

    def test_get_status_code(self):
        url = f"{BASE_URL}{GET_LIST_USERS}2"
        response = requests.get(url)
        assert response.status_code == 200

    def test_get_support_msg(self):
        url = f"{BASE_URL}{GET_LIST_USERS}2"
        response = requests.get(url)
        support_key = response.json()["support"]
        message = support_key.get("text")
        assert support_key == message


class TestSingleUser:
    def test_get_response(self):
        url = f"{BASE_URL}{SINGLE_USER}/2"
        response = requests.get(url)
        assert response.status_code == 200
        data = response.json()['data']
        get_id = data['id']
        assert get_id == 2

    def test_get_response_404(self):
        url = f"{BASE_URL}{SINGLE_USER_NOT_FOUND}"
        response = requests.get(url)
        assert response.status_code == 404
        # assert response.json() == {}


class TestPostCreate:
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    def test_create_post(self):
        url = f"{BASE_URL}{CREATE}"
        response = requests.post(url, data=self.data)
        print(response.json())

    def test_create_post_status_code(self):
        url = f"{BASE_URL}{CREATE}"
        response = requests.post(url, data=self.data)
        assert response.status_code == 201


class TestPut:
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    data_put = {
        "name": "morpheus",
        "job": "zion resident"
    }

    def test_create_and_update(self):
        url = f"https://reqres.in/api/users/"
        put_url = 'https://reqres.in/api/users/2'
        response1 = requests.post(url, data=self.data)
        print('\n', response1.json())
        assert response1.status_code == 201
        response2 = requests.put(put_url, data=self.data_put)
        assert response2.status_code == 200
        print('\n', response2.json())
        assert response1 != response2


class TestPatch:

    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    def test_create_and_del(self):
        url = f"https://reqres.in/api/users/"
        put_url = 'https://reqres.in/api/users/2'
        response1 = requests.post(url, data=self.data)
        print('\n', response1.json())
        assert response1.status_code == 201
        response2 = requests.delete(put_url)
        assert response2.status_code == 204
        print('\n', response2.text)
        assert response2.text == ''


class TestRegisterSuccessful:
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    data_wrong_email = {
        "email": "evejhholt@reqres.in",
        "password": "pistol"
    }
    data_email_is_not_valid = {
        "email": "evejhholt",
        "password": "pistol"
    }
    data_wrong_password = {
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    def test_register_successful(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data)
        print(response.json())
        assert response.status_code == 200

    def test_register_with_wrong_email(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data_wrong_email)
        print(response.json())
        assert response.json() == {'error': 'Note: Only defined users succeed registration'}
        assert response.status_code == 400

    def test_register_with_is_not_valid_email(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data_email_is_not_valid)
        print(response.json())
        assert response.json() == {'error': 'Note: Only defined users succeed registration'}
        assert response.status_code == 400

    def test_register_with_wrong_password(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data_wrong_password)
        print(response.json())
        assert response.json() == {"error": "Missing password"}
        assert response.status_code == 400

    def test_register_successful_and_get_response_by_id(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data)
        print('\n', response.json())
        assert response.status_code == 200
        get_id = response.json()['id']
        print(get_id)
        get_url = f"""https://reqres.in/api/users/{get_id}"""
        response1 = requests.get(get_url)
        print(response1)
        assert self.data['email'] == response1.json()['data']['email']

    def test_register_successful_and_verify_content_type(self):
        url = 'https://reqres.in/api/register'
        response = requests.post(url, data=self.data)
        print('\n', response.json())
        assert response.status_code == 200
        get_id = response.json()['id']
        get_url = f"""https://reqres.in/api/users/{get_id}"""
        response1 = requests.get(get_url)
        assert response1.headers['Content-Type'] == 'application/json; charset=utf-8'


class TestLoginSuccessful:
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    data_wrong_email = {
        "email": "evejhholt@reqres.in",
        "password": "pistol"
    }
    data_email_is_not_valid = {
        "email": "evejhholt",
        "password": "pistol"
    }
    data_wrong_password = {
        "email": "eve.holt@reqres.in",
        "password": ""
    }

    def test_login_successful(self):
        url = 'https://reqres.in/api/login'
        response = requests.post(url, data=self.data)
        print(response.json())
        assert response.status_code == 200
        assert response.json()['token'] == "QpwL5tke4Pnpja7X4"


class TestDelayResponse:
    def test_get_delayed_response(self):
        url = 'https://reqres.in/api/users?delay=3'
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        delay = end_time - start_time
        print('\n', delay)
        assert delay >= 3
