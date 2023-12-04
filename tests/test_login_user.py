import allure
import pytest
from data import Data as D
from helpers import Helpers as Help
from client_requests import ClientRequests as Client


class TestLoginUser:

    @allure.title('Проверка успешного создания пользователя')
    @allure.description('Логинимся с ранее зарегистрированными имэйлом и паролем, проверяем, что в ответе получаем '
                        'статус 200, в теле ответа возвращается success: true, возвращаются email и name '
                        'созданного пользователя, а также что в ответе содержатся refreshToken и accessToken')
    def test_login_with_registered_user(self, new_user):
        client = Client()
        payload = {'email': new_user['email'], 'password': new_user['password']}
        response = client.login_user(payload)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == new_user['email']
        assert response.json()['user']['name'] == new_user['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title('Проверка создания пользователя с неверным логином и паролем')
    @allure.description('Логинимся с незарегистрированными имэйлом и паролем, проверяем, что в ответе получаем '
                        'статус 401, в теле ответа возвращается сообщение success: false, '
                        'message: "email or password are incorrect"')
    def test_login_with_unregistered_email_password(self):
        client = Client()
        payload = {'email': Help.fake_email(), 'password': Help.fake_password()}
        response = client.login_user(payload)
        assert response.status_code == D.STATUS_401
        assert response.json()['success'] is False
        assert response.json()['message'] == D.ERROR_WRONG_LOGIN

    @allure.title('Проверка логина пользователя без одного из обязательных полей - без имейла или пароля')
    @allure.description('Логиним пользователя без одного из обязательных полей: без пароля, без имэйла'
                        'проверяем, что в ответе получаем статус 401, в теле ответа получаем '
                        'success: false, message: "email or password are incorrect"')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_without_one_of_mandatory_fields(self, field):
        payload = {'email': Help.fake_email(), 'password': Help.fake_password()}
        payload.pop(field)
        client = Client()
        response_create = client.login_user(payload)
        assert response_create.status_code == D.STATUS_401
        assert response_create.json()['message'] == D.ERROR_WRONG_LOGIN
