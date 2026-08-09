import allure
from src.api.order_api import OrderAPI


@allure.feature('Список заказов')
class TestOrdersList:

    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = OrderAPI.get_orders_list()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
