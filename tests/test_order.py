import pytest
import allure
from data import Urls, OrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.suite("Оформление заказа")
class TestOrder:

    @allure.title("Успешное оформление заказа через верхнюю кнопку <Заказать>")
    def test_order_via_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        data = OrderData.ORDER_DATA_SET_1

        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_personal_data_form(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            subway_station=data['subway_station'],
            phone=data['phone']
        )

        order_page.fill_rent_details_form(
            date=data['date'],
            rental_period=data['rental_period'],
            color=data['color'],
            comment=data['comment']
        )

        order_page.confirm_order()
        assert order_page.is_success_order_modal_displayed()

    @allure.title("Успешное оформление заказа через нижнюю кнопку <Заказать>")
    def test_order_via_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        data = OrderData.ORDER_DATA_SET_2

        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.fill_personal_data_form(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            subway_station=data['subway_station'],
            phone=data['phone']
        )

        order_page.fill_rent_details_form(
            date=data['date'],
            rental_period=data['rental_period'],
            color=data['color'],
            comment=data['comment']
        )

        order_page.confirm_order()
        assert order_page.is_success_order_modal_displayed()
