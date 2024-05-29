import allure

from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocator as SPL


class SignupPage(BasePage):

    @allure.step('Получить доступ к shadow_root в DOM')
    def get_shadow_root(self):
        shadow_host = self.find_element_by_locator(SPL.SHADOW_HOST)
        shadow_root = shadow_host.shadow_root
        return shadow_root
