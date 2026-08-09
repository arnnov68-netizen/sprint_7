import pytest
import allure
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password


@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Авторизация с неправильным логином')
    def test_login_wrong_login(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        wrong_login = generate_random_string(10)

        response = CourierAPI.login_courier(wrong_login, password)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title('Авторизация с неправильным паролем')
    def test_login_wrong_password(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        wrong_password = generate_random_string(10)

        response = CourierAPI.login_courier(login, wrong_password)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title('Авторизация без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_missing_field(self, missing_field):
        login = generate_random_string(10) if missing_field != 'login' else ''
        password = generate_random_string(10) if missing_field != 'password' else ''

        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_nonexistent_user(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text