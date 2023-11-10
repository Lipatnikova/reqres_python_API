"""This module is used for data generation."""
import random
from faker import Faker
from dataclasses import dataclass
from data_tests.expected_result import ExpectedCountUserList as Count


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


class DataPost:
    person = next(generated_person())

    data_post_user = {
        "name": person.name,
        "job": person.job
    }


class DataPut:
    person = next(generated_person())

    data_put_user = {
        "name": person.name,
        "job": person.job
    }
