import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проскроллить страницу к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])

    @allure.step("Ожидать, что URL содержит: {partial_url}")
    def wait_url_contains(self, partial_url):
        return self.wait.until(EC.url_contains(partial_url))
