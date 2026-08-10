import pytest
import allure
from src.api.order_api import OrderAPI
from src.data.test_data import TestData


@allure.feature('Получение заказа по номеру')
class TestGetOrder:

    @allure.title('Успешное получение заказа по треку')
    def test_get_order_by_track_success(self):
        # Создаем заказ
        order_data = TestData.ORDER_DATA.copy()
        response = OrderAPI.create_order(**order_data)
        track = response.json()["track"]

        # Получаем заказ по треку
        get_response = OrderAPI.get_order_by_track(track)

        assert get_response.status_code == 200
        assert "order" in get_response.json()
        assert get_response.json()["order"]["track"] == track

    @allure.title('Получение заказа без номера')
    def test_get_order_without_track(self):
        response = OrderAPI.get_order_by_track(None)

        assert response.status_code == 400
        assert TestData.ERROR_MESSAGES["insufficient_data_for_search"] in response.text

    @allure.title('Получение заказа с несуществующим номером')
    def test_get_order_nonexistent_track(self):
        track = 999999

        response = OrderAPI.get_order_by_track(track)

        assert response.status_code == 404
        assert TestData.ERROR_MESSAGES["order_not_found_by_track"] in response.text
