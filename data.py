
class Data:

    ERROR_ALREADY_EXISTS = 'User already exists'
    ERROR_MANDATORY_FIELD_MISSING = 'Email, password and name are required fields'
    ERROR_WRONG_LOGIN = 'email or password are incorrect'
    ERROR_NOT_AUTHORIZED = 'You should be authorised'
    ERROR_INGREDIENTS_NOT_PROVIDED = 'Ingredient ids must be provided'
    ERROR_INGREDIENTS_NOT_CORRECT = 'One or more ids provided are incorrect'

    STATUS_200 = 200
    STATUS_400 = 400
    STATUS_401 = 401
    STATUS_403 = 403
    STATUS_500 = 500

    INCORRECT_INGREDIENT_HASH = "63c1d9d71d1f82001bdaaa75"
