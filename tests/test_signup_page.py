import allure
import pytest

from locators.signup_page_locators import SignupPageLocator as SPL
from pages.signup_page import SignupPage
from sourses.data import Data
from sourses.constants import Constant
from sourses.support import generate_random_string, generate_fake_email


class TestSignupPage:

    @allure.title('Проверка невозможности заполнения поля "Имя пользователя" количеством символов меньше требуемого')
    @pytest.mark.parametrize('username_length', [5, 4])
    def test_fill_username_field_less_length_unavailable_success(self, driver, username_length):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        username_value = generate_random_string(username_length)
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(username_value)
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.click()
        message = shadow_root.find_element(*SPL.USERNAME_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_1

    @allure.title('Проверка невозможности заполнения поля "Имя пользователя" количеством символов больше требуемого')
    @pytest.mark.parametrize('username_length', [33, 34])
    def test_fill_username_field_more_length_unavailable_success(self, driver, username_length):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование имени пользователя
        username_value = generate_random_string(username_length)
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(username_value)
        # Получение ошибки
        message = shadow_root.find_element(*SPL.USERNAME_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_2

    @allure.title('Проверка невозможности использования невалидного символа в начале "Имени пользователя"')
    @pytest.mark.parametrize('username_first_invalid_simbol', ['digit', 'underlining'])
    def test_fill_username_field_first_invalid_simbol_unavailable_success(self, driver, username_first_invalid_simbol):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование имени пользователя
        username_value = generate_random_string(Constant.STRING_LEN, username_first_invalid_simbol)
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(username_value)
        # Получение ошибки
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.click()
        message = shadow_root.find_element(*SPL.USERNAME_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_1

    @allure.title('Проверка невозможности заполнения поля "Имя пользователя" невалидными символами')
    @pytest.mark.parametrize('username_invalid_simbols', ['punctuation', 'other_alf'])
    def test_fill_username_field_invalid_simbols_unavailable_success(self, driver, username_invalid_simbols):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование имени пользователя
        username_value = generate_random_string(Constant.STRING_LEN, username_invalid_simbols)
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(username_value)
        # Получение ошибки
        message = shadow_root.find_element(*SPL.USERNAME_MESSAGE)
        assert Constant.ERROR_MESSAGE_3 in message.text

    @allure.title('Проверка невозможности заполнения поля "Электронная почта" без обязательных символов')
    @pytest.mark.parametrize('email_required_simbols', ['not_dot', 'not_@'])
    def test_fill_email_field_without_required_simbol_unavailable_success(self, driver, email_required_simbols):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование email
        email_value = generate_fake_email(email_required_simbols)
        # Получение и заполнение поля "Электронный адрес"
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.send_keys(email_value)
        # Получение ошибки
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.click()
        message = shadow_root.find_element(*SPL.EMAIL_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_4

    @allure.title('Проверка невозможности заполнения поля "Пароль" количеством символов меньше требуемого')
    @pytest.mark.parametrize('password_length', [7, 6])
    def test_fill_password_field_less_length_unavailable_success(self, driver, password_length):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование пароля
        password_value = generate_random_string(password_length)
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(password_value)
        # Получение ошибки
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.click()
        message = shadow_root.find_element(*SPL.PASSWORD_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_5

    @allure.title('Проверка невозможности заполнения поля "Пароль" количеством символов больше требуемого')
    @pytest.mark.parametrize('password_length', [65, 66])
    def test_fill_password_field_more_length_unavailable_success(self, driver, password_length):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование пароля
        password_value = generate_random_string(password_length)
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(password_value)
        # Получение ошибки
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.click()
        message = shadow_root.find_element(*SPL.PASSWORD_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_6

    @allure.title('Проверка невозможности заполнения поля "Пароль" без всех типов обязательных символов')
    @pytest.mark.parametrize('password_required_types', ['not_uppercase', 'not_lowercase', 'not_digit'])
    def test_fill_password_field_without_required_types_unavailable_success(self, driver, password_required_types):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Формирование пароля
        password_value = generate_random_string(Constant.STRING_LEN, password_required_types)
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(password_value)
        # Получение ошибки
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.click()
        message = shadow_root.find_element(*SPL.PASSWORD_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_6

    @allure.title('Проверка невозможности регистрации без заполнения поля "Имя пользователя"')
    def test_signup_without_username_unavailable_success(self, driver):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Получение и заполнение поля "Электронный адрес"
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.send_keys(Data.signup_data['email'])
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(Data.signup_data['password'])
        # Получение и включение чекбокса "Пользовательское соглашение"
        checkbox = shadow_root.find_element(*SPL.USER_AGREEMENT_CHECKBOX)
        checkbox.click()
        # Клик по кнопке "Далее"
        reg_button = shadow_root.find_element(*SPL.REG_BUTTON)
        reg_button.click()
        # Получение ошибки
        message = shadow_root.find_element(*SPL.USERNAME_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_7

    @allure.title('Проверка невозможности регистрации без заполнения поля "Электронная почта"')
    def test_signup_without_email_unavailable_success(self, driver):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(Data.signup_data['username'])
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(Data.signup_data['password'])
        # Получение и включение чекбокса "Пользовательское соглашение"
        checkbox = shadow_root.find_element(*SPL.USER_AGREEMENT_CHECKBOX)
        checkbox.click()
        # Клик по кнопке "Далее"
        reg_button = shadow_root.find_element(*SPL.REG_BUTTON)
        reg_button.click()
        # Получение ошибки
        message = shadow_root.find_element(*SPL.EMAIL_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_7

    @allure.title('Проверка невозможности регистрации без заполнения поля "Пароль"')
    def test_signup_without_password_unavailable_success(self, driver):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(Data.signup_data['username'])
        # Получение и заполнение поля "Электронный адрес"
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.send_keys(Data.signup_data['email'])
        # Получение и включение чекбокса "Пользовательское соглашение"
        checkbox = shadow_root.find_element(*SPL.USER_AGREEMENT_CHECKBOX)
        checkbox.click()
        # Клик по кнопке "Далее"
        reg_button = shadow_root.find_element(*SPL.REG_BUTTON)
        reg_button.click()
        # Получение ошибки
        message = shadow_root.find_element(*SPL.PASSWORD_MESSAGE)
        assert message.text == Constant.ERROR_MESSAGE_7

    @allure.title('Проверка невозможности регистрации без галочки в чекбоксе "Пользовательское соглашение"')
    def test_signup_without_checkbox_unavailable_success(self, driver):
        signup_page = SignupPage(driver)
        signup_page.go_to_site()
        shadow_root = signup_page.get_shadow_root()
        # Получение и заполнение поля "Имя пользователя"
        username_field = shadow_root.find_element(*SPL.USERNAME_FIELD)
        username_field.send_keys(Data.signup_data['username'])
        # Получение и заполнение поля "Электронный адрес"
        email_field = shadow_root.find_element(*SPL.EMAIL_FIELD)
        email_field.send_keys(Data.signup_data['email'])
        # Получение и заполнение поля "Пароль"
        password_field = shadow_root.find_element(*SPL.PASSWORD_FIELD)
        password_field.send_keys(Data.signup_data['password'])
        # Клик по кнопке "Далее"
        reg_button = shadow_root.find_element(*SPL.REG_BUTTON)
        reg_button.click()
        # Получение ошибки
        message = shadow_root.find_element(*SPL.CHECKBOX_MESSAGE)
        assert 'error--text' in message.get_attribute('class')
