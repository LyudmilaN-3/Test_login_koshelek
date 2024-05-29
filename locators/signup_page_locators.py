from selenium.webdriver.common.by import By


class SignupPageLocator:

    SHADOW_HOST = (By.CSS_SELECTOR, "div[p1='signup']")

    # Поля для заполнения на странице регистрации
    USERNAME_FIELD = [By.CSS_SELECTOR, "input[type='text']"]
    EMAIL_FIELD = [By.CSS_SELECTOR, "input[type='email']"]
    PASSWORD_FIELD = [By.CSS_SELECTOR, "input[id='new-password']"]
    USER_AGREEMENT_CHECKBOX = [By.CSS_SELECTOR, "input[type='checkbox']"]

    # Ошибки при заполнении полей на странице регистрации
    USERNAME_MESSAGE = [By.CSS_SELECTOR, "div[data-wi='user-name'] div[data-wi='message'] span"]
    EMAIL_MESSAGE = [By.CSS_SELECTOR, "div[data-wi='identificator'] div[data-wi='message'] span"]
    PASSWORD_MESSAGE = [By.CSS_SELECTOR, "div[data-wi='password'] div[data-wi='error'] span"]
    CHECKBOX_MESSAGE = [By.CSS_SELECTOR, "div[data-wi='user-agreement'] span"]

    # Кнопка "Далее"
    REG_BUTTON = [By.CSS_SELECTOR, "div[data-wi='submit-button'] button span"]

