import allure
import pytest
from client_requests import ClientRequests as Client
from helpers import Helpers as Help
from data import Errors as E
from data import Status as S


class TestCreateUser:

    @allure.title('Проверка создания пользователя')
    @allure.description('Создаем сущность пользователя, проверяем, что в ответе получаем статус 200, в теле ответа '
                        'возвращается success: true, возвращаются email и name созданного пользователя, а также что'
                        'в ответе содержатся refreshToken и accessToken'
                        'в конце удаляем созданного пользователя')
    def test_create_new_user(self):
        email = Help.fake_email()
        password = Help.fake_password()
        name = Help.fake_name()
        payload = {"email": email, "password": password, "name": name}
        client = Client()
        response = client.create_user(payload)
        Help.check_success_response(response)
        Help.check_response_mail_name(response, email, name)
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        client.delete_user({'Authorization': response.json()['accessToken']})

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Создаем сущность пользователя, отправляем на регистрацию, далее отправляем на регистрацию '
                        'пользователя с теми же данными, проверяем, что в ответе получаем статус 403, в теле ответа '
                        'получаем success: false, message: "User already exists"')
    def test_create_same_user(self, new_user):
        payload = {"email": new_user['email'], "password": new_user['password'], "name": new_user['name']}
        client = Client()
        response = client.create_user(payload)
        assert response.status_code == S.STATUS_403
        assert response.json()['success'] is False
        assert response.json()['message'] == E.ERROR_ALREADY_EXISTS

    @allure.title('Проверка создания пользователя без одного из обязательных полей')
    @allure.description('Создаем пользователя без одного из обязательных полей: без имени, без пароля, без имэйла'
                        'проверяем, что в ответе получаем статус 403, в теле ответа получаем '
                        'success: false, message: "Email, password and name are required fields"')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_one_of_mandatory_fields(self, field):
        payload = {'email': Help.fake_email(), 'password': Help.fake_password(), 'name': Help.fake_name()}
        payload.pop(field)
        client = Client()
        response_create = client.create_user(payload)
        assert response_create.status_code == S.STATUS_403
        assert response_create.json()['message'] == E.ERROR_MANDATORY_FIELD_MISSING
