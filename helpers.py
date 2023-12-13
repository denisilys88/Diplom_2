from faker import Faker
from data import Status as S


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

    @staticmethod
    def check_success_response(response):
        assert response.status_code == S.STATUS_200
        assert response.json()['success'] is True

    @staticmethod
    def check_response_mail_name(response, email, name):
        assert response.json()['user']['email'] == email
        assert response.json()['user']['name'] == name
