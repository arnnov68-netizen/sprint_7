import pytest
import allure
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password, \
    get_courier_id


@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        courier_id = get_courier_id(login, password)

        response = CourierAPI.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без ID')
    def test_delete_courier_without_id(self):
        # Создаем неправильный URL без ID
        import requests
        response = requests.delete("https://qa-scooter.praktikum-services.ru/api/v1/courier/")

        # Ожидаем ошибку 404 или 405
        assert response.status_code in [404, 405]

    @allure.title('Удаление курьера с несуществующим ID')
    def test_delete_courier_nonexistent_id(self):
        courier_id = 999999

        response = CourierAPI.delete_courier(courier_id)

        assert response.status_code == 404
        assert "Курьера с таким id нет" in response.text