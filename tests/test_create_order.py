import pytest
import allure
from src.api.order_api import OrderAPI
from src.data.test_data import TestData


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize('color', TestData.COLOR_VARIANTS)
    def test_create_order_with_different_colors(self, color):
        order_data = TestData.ORDER_DATA.copy()
        if color:
            order_data["color"] = color

        response = OrderAPI.create_order(**order_data)

        assert response.status_code == 201
        assert "track" in response.json()
