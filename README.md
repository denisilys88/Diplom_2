В папке tests добавлены следующие классы тестов для АПИ https://stellarburgers.nomoreparties.site/api/

test_create_order::TestCreateOrder
    1 test_create_order_authorized - 'Проверка успешного создания заказа с авторизацией'
    2 test_create_order_unauthorized - 'Проверка успешного создания заказа без авторизации'
    3 test_create_order_without_ingredients_unauthorized - 'Проверка создания заказа без ингредиентов без авторизации'
    4 test_create_order_without_ingredients_authorized - 'Проверка создания заказа без ингредиентов с авторизацией'
    5 test_create_order_with_wrong_hash_ingredients - 'Проверка создания заказа с неверным хэшем ингредиентов'


test_create_user::TestCreateUser
    1 test_create_new_user - 'Проверка создания пользователя'
    2 test_create_same_user - 'Проверка создания пользователя, который уже зарегистрирован'
    3 test_create_user_without_one_of_mandatory_fields - 'Проверка создания пользователя без одного из обязательных полей'


test_get_orders_by_user::TestGetOrdersByUser
    1 test_get_orders_by_authorized_user - 'Проверка получения заказов авторизованным пользователем'
    2 test_get_orders_by_unauthorized_user - 'Проверка получения заказов неавторизованным пользователем'


test_login_user::TestLoginUser
    1 test_login_with_registered_user - 'Проверка успешного создания пользователя'
    2 test_login_with_unregistered_email_password - 'Проверка создания пользователя с неверным логином и паролем'
    3 test_login_without_one_of_mandatory_fields - Проверка логина пользователя без одного из обязательных полей - без имейла или пароля'


test_user_data_change::TestUserDataChange
    1 test_change_data_of_authorized_user - 'Проверка изменений всех данных авторизованного пользователя'
    2 test_change_email_of_authorized_user - 'Проверка изменения имейла авторизованного пользователя'
    3 test_change_password_of_authorized_user - 'Проверка изменения пароля авторизованного пользователя'
    4 test_change_name_of_authorized_user - 'Проверка изменения имени авторизованного пользователя'
    5 test_change_data_of_unauthorized_user - 'Проверка изменения данных неавторизованного пользователя'
