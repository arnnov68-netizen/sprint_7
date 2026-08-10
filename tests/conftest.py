import pytest
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string


@pytest.fixture
def create_courier_and_return_data():
    """Фикстура для создания курьера и возврата его данных"""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    response = CourierAPI.create_courier(login, password, first_name)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "first_name": first_name,
            "response": response
        }
    return None


@pytest.fixture
def create_courier_and_get_id(create_courier_and_return_data):
    """Фикстура для создания курьера и получения его ID"""
    data = create_courier_and_return_data
    if not data:
        return None

    login = data["login"]
    password = data["password"]

    login_response = CourierAPI.login_courier(login, password)

    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        return {
            "id": courier_id,
            "login": login,
            "password": password,
            "first_name": data["first_name"]
        }
    return None


@pytest.fixture
def delete_courier_after_test():
    """Фикстура для удаления курьера после теста"""
    created_couriers = []

    def _register_courier(login, password, first_name):
        response = CourierAPI.create_courier(login, password, first_name)
        if response.status_code == 201:
            # Получаем ID созданного курьера
            login_response = CourierAPI.login_courier(login, password)
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                created_couriers.append(courier_id)
        return response

    yield _register_courier

    # Удаляем всех созданных курьеров после теста
    for courier_id in created_couriers:
        CourierAPI.delete_courier(courier_id)
