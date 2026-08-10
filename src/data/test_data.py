class TestData:
    """Класс с тестовыми данными"""

    # Данные для заказов
    ORDER_DATA = {
        "first_name": "Иван",
        "last_name": "Петров",
        "address": "Москва, ул. Пушкина, д. 10",
        "metro_station": 1,
        "phone": "+7 999 999-99-99",
        "rent_time": 5,
        "delivery_date": "2024-12-31",
        "comment": "Позвонить за час"
    }

    # Варианты цветов для тестирования
    COLOR_VARIANTS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    # Тексты сообщений об ошибках
    ERROR_MESSAGES = {
        "duplicate_login": "Этот логин уже используется",
        "missing_fields": "Недостаточно данных для создания учетной записи",
        "login_not_found": "Учетная запись не найдена",
        "missing_login_data": "Недостаточно данных для входа",
        "courier_not_found": "Курьера с таким id нет",
        "courier_not_exists": "Курьера с таким id не существует",
        "order_not_found": "Заказа с таким id нет",
        "order_not_exists": "Заказа с таким id не существует",
        "order_not_found_by_track": "Заказ не найден",
        "insufficient_data_for_search": "Недостаточно данных для поиска"
    }
