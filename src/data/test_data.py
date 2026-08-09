class TestData:
    """Класс с тестовыми данными"""

    # Данные для заказов - используем правильные имена параметров
    ORDER_DATA = {
        "first_name": "Иван",  # изменено с firstName на first_name
        "last_name": "Петров",  # изменено с lastName на last_name
        "address": "Москва, ул. Пушкина, д. 10",
        "metro_station": 1,  # изменено с metroStation на metro_station
        "phone": "+7 999 999-99-99",
        "rent_time": 5,  # изменено с rentTime на rent_time
        "delivery_date": "2024-12-31",  # изменено с deliveryDate на delivery_date
        "comment": "Позвонить за час"
    }

    # Варианты цветов для тестирования
    COLOR_VARIANTS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]