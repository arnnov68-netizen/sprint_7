import random
import string


def generate_random_string(length=10):
    """Генерация случайной строки из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_data():
    """
    Генерация данных для нового курьера

    Returns:
        tuple: (login, password, first_name)
    """
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return login, password, first_name
