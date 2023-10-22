"""This module is used to generate data for tests."""
from faker import Faker
from data.data import Person

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
