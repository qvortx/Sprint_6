import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Скроллим к разделу 'Вопросы о важном'")
    def scroll_to_questions_section(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_HEADER)

    @allure.step("Кликаем на вопрос #{index}")
    def click_question(self, index):
        locator = (MainPageLocators.QUESTION_HEADING[0], MainPageLocators.QUESTION_HEADING[1].format(index))
        self.click_element(locator)

    @allure.step("Получаем текст ответа #{index}")
    def get_answer_text(self, index):
        locator = (MainPageLocators.ANSWER_PANEL[0], MainPageLocators.ANSWER_PANEL[1].format(index))
        return self.get_text(locator)

    @allure.step("Кликнуть по верхней кнопке «Заказать» в шапке")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке «Заказать»")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть по логотипу «Самокат»")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу «Яндекс»")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
