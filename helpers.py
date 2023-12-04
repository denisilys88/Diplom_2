from faker import Faker


class Helpers:

    @staticmethod
    def fake_name():
        faker = Faker()
        return faker.name()

    @staticmethod
    def fake_password():
        faker = Faker()
        return faker.password()

    @staticmethod
    def fake_email():
        faker = Faker()
        return faker.email()
