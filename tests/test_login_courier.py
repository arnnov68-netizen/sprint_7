import pytest
import allure
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string, generate_courier_data
from src.data.test_data import TestData


@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        login = courier_data["login"]
        password = courier_data["password"]
        courier_id = courier_data["id"]

        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 200
        assert "id" in response.json()

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Авторизация с неправильным логином')
    def test_login_wrong_login(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        password = courier_data["password"]
        courier_id = courier_data["id"]
        wrong_login = generate_random_string(10)

        response = CourierAPI.login_courier(wrong_login, password)

        assert response.status_code == 404
        assert TestData.ERROR_MESSAGES["login_not_found"] in response.text

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Авторизация с неправильным паролем')
    def test_login_wrong_password(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        login = courier_data["login"]
        courier_id = courier_data["id"]
        wrong_password = generate_random_string(10)

        response = CourierAPI.login_courier(login, wrong_password)

        assert response.status_code == 404
        assert TestData.ERROR_MESSAGES["login_not_found"] in response.text

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Авторизация без обязательных полей')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), '')
    ])
    def test_login_missing_field(self, login, password):
        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 400
        assert TestData.ERROR_MESSAGES["missing_login_data"] in response.text

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_nonexistent_user(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        response = CourierAPI.login_courier(login, password)

        assert response.status_code == 404
        assert TestData.ERROR_MESSAGES["login_not_found"] in response.text
