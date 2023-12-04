import allure
import requests


class ClientRequests:

    def __init__(self):
        self.host = 'https://stellarburgers.nomoreparties.site/api/'

    @allure.step('вызываем нужный метод requests по переданным параметрам')
    def make_request(self, path, type, payload=None, headers_data=None):
        response = ''
        url = f'{self.host}{path}'
        if type == 'post':
            response = requests.post(url, data=payload, headers=headers_data)
        elif type == 'get':
            response = requests.get(url, data=payload, headers=headers_data)
        elif type == 'delete':
            response = requests.delete(url)
        elif type == 'put':
            response = requests.put(url, data=payload)
        elif type == 'patch':
            response = requests.patch(url, data=payload, headers=headers_data)
        return response

    @allure.step('вызываем метод make_request для ручки создания пользователя')
    def create_user(self, payload):
        path = f"auth/register"
        return self.make_request(path, 'post', payload)

    @allure.step('вызываем метод make_request для ручки авторизации пользователя')
    def login_user(self, payload):
        path = f"auth/login"
        return self.make_request(path, 'post', payload)

    @allure.step('вызываем метод make_request для ручки обновления данных пользователя')
    def update_user_data(self, payload, headers_data=None):
        path = f"auth/user"
        return self.make_request(path, 'patch', payload, headers_data)

    @allure.step('вызываем метод make_request для ручки получения данных об ингредиентах')
    def get_ingredients_data(self):
        path = f"ingredients"
        return self.make_request(path, 'get')

    @allure.step('вызываем метод make_request для ручки создания заказа')
    def create_order(self, payload, headers_data=None):
        path = f"orders"
        return self.make_request(path, 'post', payload, headers_data)

    @allure.step('вызываем метод make_request для ручки получения заказов пользователя')
    def get_orders_by_user(self, payload=None, headers_data=None):
        path = f"orders"
        return self.make_request(path, 'get', payload, headers_data)
