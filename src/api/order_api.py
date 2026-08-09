import requests
from src.api.endpoints import Endpoints


class OrderAPI:
    """Класс для работы с API заказов"""

    @staticmethod
    def create_order(first_name, last_name, address, metro_station, phone,
                     rent_time, delivery_date, comment, color=None):
        """Создание заказа"""
        payload = {
            "firstName": first_name,  # API ожидает firstName
            "lastName": last_name,  # API ожидает lastName
            "address": address,
            "metroStation": metro_station,  # API ожидает metroStation
            "phone": phone,
            "rentTime": rent_time,  # API ожидает rentTime
            "deliveryDate": delivery_date,  # API ожидает deliveryDate
            "comment": comment
        }
        if color:
            payload["color"] = color

        response = requests.post(Endpoints.ORDERS, json=payload)
        return response

    @staticmethod
    def get_orders_list():
        """Получение списка заказов"""
        response = requests.get(Endpoints.ORDERS_LIST)
        return response

    @staticmethod
    def cancel_order(track):
        """Отмена заказа"""
        payload = {"track": track}
        response = requests.put(Endpoints.ORDERS_CANCEL, data=payload)
        return response

    @staticmethod
    def accept_order(order_id, courier_id):
        """Принятие заказа курьером"""
        url = Endpoints.get_order_accept_url(order_id, courier_id)
        response = requests.put(url)
        return response

    @staticmethod
    def get_order_by_track(track):
        """Получение заказа по треку"""
        params = {"t": track}
        response = requests.get(Endpoints.ORDER_GET, params=params)
        return response