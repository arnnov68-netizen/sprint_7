import pytest
import allure
from src.api.courier_api import CourierAPI
from src.helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = CourierAPI.create_courier(login, password, first_name)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # Первое создание
        response1 = CourierAPI.create_courier(login, password, first_name)
        assert response1.status_code == 201

        # Второе создание с теми же данными
        response2 = CourierAPI.create_courier(login, password, first_name)
        assert response2.status_code == 409
        assert "Этот логин уже используется" in response2.text

    @allure.title('Создание курьера без обязательного поля')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, missing_field):
        login = generate_random_string(10) if missing_field != 'login' else ''
        password = generate_random_string(10) if missing_field != 'password' else ''
        first_name = generate_random_string(10)

        response = CourierAPI.create_courier(login, password, first_name)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text

    @allure.title('Создание курьера без firstName (необязательное поле)')
    def test_create_courier_without_first_name(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        response = CourierAPI.create_courier(login, password)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание курьера с существующим логином')
    def test_create_courier_existing_login(self):
        # Создаем первого курьера
        login = generate_random_string(10)
        password1 = generate_random_string(10)
        CourierAPI.create_courier(login, password1)

        # Пытаемся создать второго с тем же логином
        password2 = generate_random_string(10)
        response = CourierAPI.create_courier(login, password2)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text