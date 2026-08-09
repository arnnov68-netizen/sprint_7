import pytest
import allure
from src.api.order_api import OrderAPI
from src.data.test_data import TestData


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с цветом BLACK')
    def test_create_order_black_color(self):
        order_data = TestData.ORDER_DATA.copy()
        order_data["color"] = ["BLACK"]

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Создание заказа с цветом GREY')
    def test_create_order_grey_color(self):
        order_data = TestData.ORDER_DATA.copy()
        order_data["color"] = ["GREY"]

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Создание заказа с двумя цветами')
    def test_create_order_both_colors(self):
        order_data = TestData.ORDER_DATA.copy()
        order_data["color"] = ["BLACK", "GREY"]

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Создание заказа без указания цвета')
    def test_create_order_without_color(self):
        order_data = TestData.ORDER_DATA.copy()

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Параметризованный тест создания заказа с разными цветами')
    @pytest.mark.parametrize('color', TestData.COLOR_VARIANTS)
    def test_create_order_with_different_colors(self, color):
        order_data = TestData.ORDER_DATA.copy()
        if color:
            order_data["color"] = color

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()