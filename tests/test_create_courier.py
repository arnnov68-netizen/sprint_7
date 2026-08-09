import pytest
import allure
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string, generate_courier_data
from src.data.test_data import TestData


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    def test_create_courier_success(self, delete_courier_after_test):
        login, password, first_name = generate_courier_data()

        response = delete_courier_after_test(login, password, first_name)
        courier_id = CourierAPI.login_courier(login, password).json().get("id")

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        login, password, first_name = generate_courier_data()

        # Первое создание
        response1 = CourierAPI.create_courier(login, password, first_name)
        assert response1.status_code == 201
        courier_id = CourierAPI.login_courier(login, password).json().get("id")

        # Второе создание с теми же данными
        response2 = CourierAPI.create_courier(login, password, first_name)
        assert response2.status_code == 409
        assert TestData.ERROR_MESSAGES["duplicate_login"] in response2.text

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Создание курьера без обязательного поля')
    @pytest.mark.parametrize('login, password, expected_error', [
        ('', generate_random_string(10), TestData.ERROR_MESSAGES["missing_fields"]),
        (generate_random_string(10), '', TestData.ERROR_MESSAGES["missing_fields"])
    ])
    def test_create_courier_missing_field(self, login, password, expected_error):
        first_name = generate_random_string(10)

        response = CourierAPI.create_courier(login, password, first_name)

        assert response.status_code == 400
        assert expected_error in response.text

    @allure.title('Создание курьера без firstName (необязательное поле)')
    def test_create_courier_without_first_name(self, delete_courier_after_test):
        login, password, _ = generate_courier_data()

        response = delete_courier_after_test(login, password, None)
        courier_id = CourierAPI.login_courier(login, password).json().get("id")

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)
