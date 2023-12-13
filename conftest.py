import pytest
from client_requests import ClientRequests as Client
from helpers import Helpers as Help
from data import Status as S


@pytest.fixture
def new_user():
    email = Help.fake_email()
    password = Help.fake_password()
    name = Help.fake_name()

    payload = {"email": email, "password": password, "name": name}

    client = Client()
    response = client.create_user(payload)

    info_response = {'email': email, 'password': password, 'name': name, 'status_code': response.status_code,
                     'json': response.json()}

    if response.status_code == S.STATUS_200:
        yield info_response
        client.delete_user({'Authorization': info_response['json']['accessToken']})
    else:
        raise Exception('не получен успешный статус 200 при попытке создания нового пользователя')


@pytest.fixture()
def get_ingredient():
    client = Client()
    response = client.get_ingredients_data()
    if response.status_code == S.STATUS_200:
        yield response
    else:
        raise Exception('не получен успешный статус 200 при попытке получить данные об ингридиентах')
