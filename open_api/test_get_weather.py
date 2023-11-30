import logging
from open_api.api import Request
from open_api.data_api.data_for_tests import DataForTests as Data
from open_api.data_api.data_for_tests import StatusCode as Code
from open_api.data_api.data_for_tests import ExpectedText as Text
from open_api.api import Calculations


logger = logging.getLogger("api")


class TestGetWeather:
    def test_weather_forecast_status_code(self):
        response = Request.get(f'?zip={Data.POSTAL_CODE},{Data.COUNTRY_CODE}&appid={Data.API_KEI}')
        response_status = response.status_code
        assert response_status == Code.STATUS_CODE_OK, logger.warning('Response status code is incorrect')

    def test_login_successful_verify_content_type(self):
        response = Request.get(f'?zip={Data.POSTAL_CODE},{Data.COUNTRY_CODE}&appid={Data.API_KEI}')
        logger.info(response.headers['Content-Type'])
        assert Text.content_type in response.headers['Content-Type'], \
            logger.warning('The headers Content-Type is wrong.')

    def test_get_weather_forecast_verify_temperature(self):
        response = Request.get(f'?zip={Data.POSTAL_CODE},{Data.COUNTRY_CODE}&appid={Data.API_KEI}')
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        logger.info(temperature)
        lower_bound, upper_bound = Calculations.get_temperature_calculation(self, temperature)
        assert lower_bound <= temperature <= upper_bound, logger.warning(f"Temperature outside 10% range{temperature}")
