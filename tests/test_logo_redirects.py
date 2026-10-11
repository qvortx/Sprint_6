import allure
from data import Urls
from pages.main_page import MainPage


@allure.suite("Редиректы по кликам на логотипы")
class TestLogoRedirects:

    @allure.title("Переход на главную страницу при клике на логотип <Самокат>")
    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        
        main_page.open_url(Urls.ORDER_URL)
        main_page.accept_cookies()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title("Открытие Дзена в новой вкладке при клике на логотип <Яндекс>")
    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        
        main_page.switch_to_new_tab()
        main_page.wait_url_contains("dzen.ru")

        assert "dzen.ru" in main_page.get_current_url()
