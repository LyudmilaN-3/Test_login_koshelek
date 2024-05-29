import allure
import random
import string
from faker import Faker

from sourses.data import Data

fake = Faker('ru_RU')


@allure.step('Формирование рандомной строки для полей "Имя пользователя" и "Пароль"')
def generate_random_string(length, value=None):
    random_string = (''.join(random.choices(string.ascii_letters, k=1)) +
                     ''.join(random.choices(string.ascii_letters + string.digits, k=length-1)))
    if value is not None:
        # Формирование строки с цифрой в начале
        if value == 'digit':
            random_string_1 = ''.join(random.choices(string.digits, k=1)) + random_string[1:11]
            return random_string_1
        # Формирование строки с нижним подчеркиванием в начале
        if value == 'underlining':
            random_string_1 = '_' + random_string[1:11]
            return random_string_1
        # Формирование строки со знаками препинания и спецсимволами
        if value == 'punctuation':
            punctuation_str = ''.join(random.choices(string.punctuation, k=5))
            punctuation_str.replace('_', '')
            random_string_1 = random_string[:5] + punctuation_str[0] + random_string[6:11]
            return random_string_1
        # Формирование строки с символами других алфавитов и иероглифами
        if value == 'other_alf':
            random_string_1 = random_string[:5] + ''.join(random.choices(Data.alf_str, k=1)) + random_string[6:11]
            return random_string_1
        # Формирование строки без заглавных букв
        if value == 'not_uppercase':
            random_string_1 = random_string.lower()
            print(random_string)
            print(random_string_1)
            return random_string_1
        # Формирование строки без прописных букв
        if value == 'not_lowercase':
            random_string_1 = random_string.upper()
            print(random_string)
            print(random_string_1)
            return random_string_1
        # Формирование строки без цифр
        if value == 'not_digit':
            random_string_1 = ''.join(random.choices(string.ascii_letters, k=length))
            print(random_string_1)
            return random_string_1
    return random_string


@allure.step('Формирование фейкового email для поля "Электронный адрес"')
def generate_fake_email(value):
    fake_email = fake.email()
    # Формирование email без точки в домене
    if value == 'not_dot':
        fake_email_1 = fake_email.replace('.', '')
        return fake_email_1
    # Формирование email без @
    if value == 'not_@':
        fake_email_1 = fake_email.replace('@', '')
        return fake_email_1
    return fake_email
