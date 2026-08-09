import pytest
import allure
import requests
from src.api.courier_api import CourierAPI
from src.data.test_data import TestData


@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        courier_id = courier_data["id"]

        response = CourierAPI.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удаление курьера без ID')
    def test_delete_courier_without_id(self):
        response = requests.delete("https://qa-scooter.praktikum-services.ru/api/v1/courier/")

        assert response.status_code in [404, 405]

    @allure.title('Удаление курьера с несуществующим ID')
    def test_delete_courier_nonexistent_id(self):
        courier_id = 999999

        response = CourierAPI.delete_courier(courier_id)

        assert response.status_code == 404
        assert TestData.ERROR_MESSAGES["courier_not_found"] in response.text
