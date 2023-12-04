import allure
from data import Data as D
from client_requests import ClientRequests as Client


class TestGetOrdersByUser:

    @allure.title('Проверка получения заказов авторизованным пользователем')
    @allure.description('Получаем информацию о заказе авторизованным пользователем, '
                        'проверяем, что в ответе получаем статус 200, в теле ответа возвращаются success: true, '
                        'список orders, total и totalToday')
    def test_get_orders_by_authorized_user(self, new_user, get_ingredient):
        client = Client()
        header = {'Authorization': new_user['json']['accessToken']}
        response = client.get_orders_by_user({}, header)
        assert response.status_code == D.STATUS_200
        assert response.json()['success'] is True
        assert isinstance(response.json()['orders'], list)
        assert 'total' in response.json()
        assert 'totalToday' in response.json()

    @allure.title('Проверка получения заказов неавторизованным пользователем')
    @allure.description('Пробуем получить список заказов неавторизованным пользователем,'
                        'проверяем, что в ответе получаем статус 401 '
                        'в теле ответа возвращается success: false, message: you should be authorised')
    def test_get_orders_by_unauthorized_user(self):
        client = Client()
        response = client.get_orders_by_user({}, '')
        assert response.status_code == D.STATUS_401
        assert response.json()['message'] == D.ERROR_NOT_AUTHORIZED
