import allure
from client_requests import ClientRequests as Client
from helpers import Helpers as Help
from data import Data as D


class TestUserDataChange:

    @allure.title('Проверка изменений всех данных авторизованного пользователя')
    @allure.description('Меняем все данные авторизованного пользователя: email, name, password, '
                        'проверяем, что в ответе получаем статус 200, в теле ответа возвращается success: true '
                        'и возвращаются обновленные email и name'
                        'далее пробуем авторизоваться с обновленным email и password, '
                        'ожидаем успешную авторизацию')
    def test_change_data_of_authorized_user(self, new_user):
        client = Client()
        email = Help.fake_email()
        name = Help.fake_name()
        password = Help.fake_password()
        payload = {"email": email, "password": password, "name": name}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.update_user_data(payload, header)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == email
        assert response.json()['user']['name'] == name
        payload_login = {'email': email, 'password': password}
        response_login = client.login_user(payload_login)
        assert response_login.status_code == D.STATUS_200

    @allure.title('Проверка изменения имейла авторизованного пользователя')
    @allure.description('Меняем email авторизованного пользователя, проверяем, что в ответе получаем статус 200, '
                        'в теле ответа возвращается success: true и возвращаются обновленный email '
                        'и ранее зарегистрированный name, далее пробуем авторизоваться с обновленным email '
                        'ожидаем успешную авторизацию с обновленными данными')
    def test_change_email_of_authorized_user(self, new_user):
        client = Client()
        email = Help.fake_email()
        payload = {"email": email}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.update_user_data(payload, header)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == email
        assert response.json()['user']['name'] == new_user['name']
        payload_login = {'email': email, 'password': new_user['password']}
        response_login = client.login_user(payload_login)
        assert response_login.status_code == D.STATUS_200

    @allure.title('Проверка изменения пароля авторизованного пользователя')
    @allure.description('Меняем password авторизованного пользователя, проверяем, что в ответе получаем статус 200, '
                        'в теле ответа возвращается success: true и ранее зарегистрированные name и email, '
                        'далее пробуем авторизоваться с обновленным password и ранее зарегистрированным email '
                        'ожидаем успешную авторизацию с обновленными данными')
    def test_change_password_of_authorized_user(self, new_user):
        client = Client()
        password = Help.fake_password()
        payload = {"password": password}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.update_user_data(payload, header)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == new_user['email']
        assert response.json()['user']['name'] == new_user['name']
        payload_login = {'email': new_user['email'], 'password': password}
        response_login = client.login_user(payload_login)
        assert response_login.status_code == D.STATUS_200

    @allure.title('Проверка изменения имени авторизованного пользователя')
    @allure.description('Меняем name авторизованного пользователя, проверяем, что в ответе получаем статус 200, '
                        'в теле ответа возвращается success: true и возвращаются ранее зарегистрированный email '
                        'и обновленный name')
    def test_change_name_of_authorized_user(self, new_user):
        client = Client()
        name = Help.fake_name()
        payload = {"name": name}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.update_user_data(payload, header)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == new_user['email']
        assert response.json()['user']['name'] == name

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    @allure.description('Меняем данные зарегистрированного, но неавторизованного пользователя, '
                        'отправляем на изменение поля name и email, без accessToken'
                        'проверяем, что в ответе получаем статус 401, '
                        'в теле ответа возвращается success: false, message:"You should be authorised"')
    def test_change_data_of_unauthorized_user(self, new_user):
        client = Client()
        payload = {"email": new_user['email'], 'password': Help.fake_password(), 'name': Help.fake_name()}
        response = client.update_user_data(payload)
        assert response.status_code == D.STATUS_401
        assert response.json()['message'] == D.ERROR_NOT_AUTHORIZED
