import random
import string
import requests
from src.api.endpoints import Endpoints


def generate_random_string(length=10):
    """Генерация случайной строки из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password():
    """
    Регистрация нового курьера и возврат его данных

    Returns:
        list: [login, password, first_name] или пустой список при ошибке
    """
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Endpoints.COURIER_CREATE, data=payload)

    if response.status_code == 201:
        login_pass.extend([login, password, first_name])

    return login_pass


def get_courier_id(login, password):
    """Получение ID курьера по логину и паролю"""
    payload = {"login": login, "password": password}
    response = requests.post(Endpoints.COURIER_LOGIN, data=payload)

    if response.status_code == 200:
        return response.json().get("id")
    return None