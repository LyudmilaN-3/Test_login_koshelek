import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sourses.constants import Constant


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Открыть страницу регистрации "Кошелёк.ру" '
                 f'{Constant.MAIN_URL}{Constant.SIGN_UP_PATH_URL}')
    def go_to_site(self):
        return self.driver.get(Constant.MAIN_URL+Constant.SIGN_UP_PATH_URL)

    def find_element_by_locator(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f'Элемент не найден по локатору - {[*locator]}')
