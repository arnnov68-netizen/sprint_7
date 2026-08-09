import pytest
import allure
import requests
from src.api.order_api import OrderAPI
from src.api.courier_api import CourierAPI
from src.data.test_data import TestData
from src.helpers.courier_helper import generate_courier_data


@allure.feature('Принятие заказа курьером')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        courier_id = courier_data["id"]

        # Создаем заказ
        order_data = TestData.ORDER_DATA.copy()
        response = OrderAPI.create_order(**order_data)
        track = response.json()["track"]

        # Получаем order_id из трека
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]

        # Принимаем заказ
        accept_response = OrderAPI.accept_order(order_id, courier_id)

        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)

    @allure.title('Принятие заказа без ID курьера')
    def test_accept_order_without_courier_id(self):
        # Создаем заказ
        order_data = TestData.ORDER_DATA.copy()
        response = OrderAPI.create_order(**order_data)
        track = response.json()["track"]

        # Получаем order_id
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]

        # Принимаем заказ без ID курьера
        url = f"https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}"
        accept_response = requests.put(url)

        assert accept_response.status_code in [400, 500]

    @allure.title('Принятие заказа с неверным ID курьера')
    def test_accept_order_wrong_courier_id(self):
        # Создаем заказ
        order_data = TestData.ORDER_DATA.copy()
        response = OrderAPI.create_order(**order_data)
        track = response.json()["track"]

        # Получаем order_id
        order_response = OrderAPI.get_order_by_track(track)
        order_id = order_response.json()["order"]["id"]

        # Принимаем заказ с неверным ID курьера
        accept_response = OrderAPI.accept_order(order_id, 999999)

        assert accept_response.status_code == 404
        assert (TestData.ERROR_MESSAGES["courier_not_found"] in accept_response.text or
                TestData.ERROR_MESSAGES["courier_not_exists"] in accept_response.text)

    @allure.title('Принятие заказа без ID заказа')
    def test_accept_order_without_order_id(self):
        # Пытаемся принять заказ без ID заказа
        url = "https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/"
        response = requests.put(url)

        assert response.status_code in [404, 405]

    @allure.title('Принятие заказа с неверным ID заказа')
    def test_accept_order_wrong_order_id(self, create_courier_and_get_id):
        courier_data = create_courier_and_get_id
        courier_id = courier_data["id"]

        # Принимаем заказ с неверным ID
        accept_response = OrderAPI.accept_order(999999, courier_id)

        assert accept_response.status_code == 404
        assert (TestData.ERROR_MESSAGES["order_not_found"] in accept_response.text or
                TestData.ERROR_MESSAGES["order_not_exists"] in accept_response.text)

        # Удаляем курьера
        CourierAPI.delete_courier(courier_id)
