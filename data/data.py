"""This module is used for data generation."""
import random
from faker import Faker
from dataclasses import dataclass
from data.expected_result import ExpectedCountUserList as Count


@dataclass
class Person:
    """Data class for person generation."""
    name: str = None
    job: str = None
    email: str = None
    password: str = None


def generated_person():
    """
    Generation of data about a person with the Faker library.
       :returns: person generator object
    """
    yield Person(
        name=Faker().first_name(),
        job=Faker().job(),
        email=Faker().email(),
        password=Faker().password()
    )


def random_num_user():
    return random.randint(1, Count.COUNT_USERS)


class DataCreateUser:
    person = next(generated_person())

    data_create_user = {
        "name": person.name,
        "job": person.job
    }


class DataUpdateUser:
    person = next(generated_person())

    data_update_user = {
        "name": person.name,
        "job": person.job
    }


class DataRegisterUser:
    person = next(generated_person())

    data_register_user = {
        # "email": person.email,
        "email": "eve.holt@reqres.in",
        "password": person.password
    }

    data_register_user_wrong = {
        "email": "sydney@fife"
    }

    data_register_user_wrong_v2 = {
        "email": "eve.holt@reqres",
        "password": person.password
    }


class DataLoginUser:
    data_login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    data_login_wrong_email = {
        "email": "peter@klaven"
    }
