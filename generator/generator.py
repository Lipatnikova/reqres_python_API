"""This module is used to generate data for tests."""
import random
from faker import Faker
from data.data import Person
from data.expected_result import ExpectedCountUserList as Count

faker = Faker()
Faker.seed()


def generated_person():
    """
    Generation of data about a person with the Faker library.
       :returns: person generator object
    """
    yield Person(
        name=faker.first_name(),
        job=faker.job(),
        email=faker.email(),
        password=faker.password()
    )


def random_num_user():
    return random.randint(1, Count.COUNT_USERS)
