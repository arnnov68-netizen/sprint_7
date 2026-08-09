import requests
from src.api.endpoints import Endpoints


class CourierAPI:
    """Класс для работы с API курьера"""

    @staticmethod
    def create_courier(login, password, first_name=None):
        """Создание курьера"""
        payload = {"login": login, "password": password}
        if first_name:
            payload["firstName"] = first_name

        response = requests.post(Endpoints.COURIER_CREATE, data=payload)
        return response

    @staticmethod
    def login_courier(login, password):
        """Авторизация курьера"""
        payload = {"login": login, "password": password}
        response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
        return response

    @staticmethod
    def delete_courier(courier_id):
        """Удаление курьера"""
        url = Endpoints.get_courier_delete_url(courier_id)
        response = requests.delete(url)
        return response