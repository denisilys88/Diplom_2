import allure
from client_requests import ClientRequests as Client
from data import Errors as E
from data import Status as S
from data import Hash as H
from helpers import Helpers as Help


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа с авторизацией')
    @allure.description('Отправляем запрос на создание заказа с 2-я ингредиентами с авторизацией'
                        'проверяем, что в ответе получаем статус 200, в теле ответа возвращается success: true '
                        'в поле name возвращается название бургера, '
                        'в поле order - ingredients возвращается список ингредиентов заказа'
                        'в поле order - number возвращается номер заказа'
                        'в поле order - price возвращается цена заказа'
                        'в блоке order возвращается id заказа'
                        'в поле order - status возвращается "done"'
                        'в поле order - owner - name возвращается имя пользователя'
                        'в поле order - owner - email возвращается имейл пользователя')
    def test_create_order_authorized(self, get_ingredient, new_user):
        client = Client()
        ingredient_1 = get_ingredient.json()['data'][0]['_id']
        ingredient_2 = get_ingredient.json()['data'][1]['_id']
        payload = {"ingredients": [ingredient_1, ingredient_2]}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.create_order(payload, header)
        Help.check_success_response(response)
        assert 'бургер' in response.json()['name']
        assert isinstance(response.json()['order']['ingredients'], list)
        assert isinstance(response.json()['order']['number'], int)
        assert isinstance(response.json()['order']['price'], int)
        assert '_id' in response.json()['order']
        assert response.json()['order']['status'] == 'done'
        assert response.json()['order']['owner']['name'] == new_user['name']
        assert response.json()['order']['owner']['email'] == new_user['email']

    @allure.title('Проверка успешного создания заказа без авторизации')
    @allure.description('Отправляем запрос на создание заказа с 2-я ингредиентами без авторизации'
                        'проверяем, что в ответе получаем статус 200, в теле ответа возвращается success: true '
                        'в поле name возвращается название бургера, в поле order - number возвращается номер заказа')
    def test_create_order_unauthorized(self, get_ingredient):
        client = Client()
        ingredient_1 = get_ingredient.json()['data'][0]['_id']
        ingredient_2 = get_ingredient.json()['data'][1]['_id']
        payload = {"ingredients": [ingredient_1, ingredient_2]}
        response = client.create_order(payload)
        Help.check_success_response(response)
        assert 'бургер' in response.json()['name']
        assert isinstance(response.json()['order']['number'], int)

    @allure.title('Проверка создания заказа без ингредиентов без авторизации')
    @allure.description('Отправляем запрос на создание заказа без ингредиентов без авторизации'
                        'проверяем, что в ответе получаем статус 400, в теле ответа возвращается сообщение '
                        '"success": false, "message": "Ingredient ids must be provided"')
    def test_create_order_without_ingredients_unauthorized(self):
        client = Client()
        payload = {"ingredients": [""]}
        response = client.create_order(payload)
        assert response.status_code == S.STATUS_400
        assert response.json()['message'] == E.ERROR_INGREDIENTS_NOT_PROVIDED

    @allure.title('Проверка создания заказа без ингредиентов с авторизацией')
    @allure.description('Отправляем запрос на создание заказа без ингредиентов с авторизацией'
                        'проверяем, что в ответе получаем статус 400, в теле ответа возвращается сообщение '
                        '"success": false, "message": "Ingredient ids must be provided"')
    def test_create_order_without_ingredients_authorized(self, new_user):
        client = Client()
        payload = {"ingredients": [""]}
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.create_order(payload, header)
        assert response.status_code == S.STATUS_400
        assert response.json()['message'] == E.ERROR_INGREDIENTS_NOT_PROVIDED

    @allure.title('Проверка создания заказа с неверным хэшем ингредиентов')
    @allure.description('Отправляем запрос на создание заказа с неверным хэшем ингредиентов'
                        'проверяем, что в ответе получаем статус 500, в теле ответа возвращается сообщение '
                        '"success": false, "message": "One or more ids provided are incorrect"')
    def test_create_order_with_wrong_hash_ingredients(self):
        client = Client()
        payload = {"ingredients": [H.INCORRECT_INGREDIENT_HASH]}
        response = client.create_order(payload)
        assert response.json()['success'] is False
        assert response.json()['message'] == E.ERROR_INGREDIENTS_NOT_CORRECT
        assert response.status_code == S.STATUS_500  # must be 500 by documentation
