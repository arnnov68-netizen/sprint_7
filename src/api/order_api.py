import requests
import allure
from src.api.endpoints import Endpoints


class OrderAPI:
    """Класс для работы с API заказов"""

    @staticmethod
    @allure.step("Создание заказа для {first_name} {last_name}")
    def create_order(first_name, last_name, address, metro_station, phone,
                     rent_time, delivery_date, comment, color=None):
        """Создание заказа"""
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        if color:
            payload["color"] = color

        response = requests.post(Endpoints.ORDERS, json=payload)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders_list():
        """Получение списка заказов"""
        response = requests.get(Endpoints.ORDERS_LIST)
        return response

    @staticmethod
    @allure.step("Отмена заказа по треку: {track}")
    def cancel_order(track):
        """Отмена заказа"""
        payload = {"track": track}
        response = requests.put(Endpoints.ORDERS_CANCEL, data=payload)
        return response

    @staticmethod
    @allure.step("Принятие заказа ID: {order_id} курьером ID: {courier_id}")
    def accept_order(order_id, courier_id):
        """Принятие заказа курьером"""
        url = Endpoints.get_order_accept_url(order_id, courier_id)
        response = requests.put(url)
        return response

    @staticmethod
    @allure.step("Получение заказа по треку: {track}")
    def get_order_by_track(track):
        """Получение заказа по треку"""
        params = {"t": track}
        response = requests.get(Endpoints.ORDER_GET, params=params)
        return response
