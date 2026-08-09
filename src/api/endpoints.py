class Endpoints:
    """Класс с URL-адресами эндпоинтов API"""

    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # Эндпоинты для курьера
    COURIER_CREATE = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN = f"{BASE_URL}/api/v1/courier/login"

    # Эндпоинты для заказов
    ORDERS = f"{BASE_URL}/api/v1/orders"
    ORDERS_CANCEL = f"{BASE_URL}/api/v1/orders/cancel"
    ORDERS_LIST = f"{BASE_URL}/api/v1/orders"
    ORDER_GET = f"{BASE_URL}/api/v1/orders/track"

    @staticmethod
    def get_courier_delete_url(courier_id):
        """Получить URL для удаления курьера"""
        return f"{Endpoints.BASE_URL}/api/v1/courier/{courier_id}"

    @staticmethod
    def get_order_accept_url(order_id, courier_id):
        """Получить URL для принятия заказа"""
        return f"{Endpoints.BASE_URL}/api/v1/orders/accept/{order_id}?courierId={courier_id}"
