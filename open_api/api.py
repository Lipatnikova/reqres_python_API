import logging
import requests
from open_api.data_api.data_urls import Urls

logger = logging.getLogger("api")


class Request:

    @classmethod
    def get(cls, endpoint, params=None):
        url = f"{Urls.BASE_URL}{endpoint}"
        response = requests.get(url, params=params)
        logger.info(response.json())
        return response


class Calculations:
    # Get  the results temperature in a range of 10%
    def get_temperature_calculation(self, temperature):
        lower_bound = temperature * 0.9
        upper_bound = temperature * 1.1
        return lower_bound, upper_bound
