from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    QUESTIONS_HEADER = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")

    @staticmethod
    def question_locator(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")
