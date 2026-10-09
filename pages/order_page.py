import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить первую страницу формы заказа <Для кого самокат>")
    def fill_personal_data_form(self, first_name, last_name, address, subway_station, phone):
        self.find_element(OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

        subway_field = self.find_element(OrderPageLocators.SUBWAY_STATION_INPUT)
        subway_field.click()
        subway_field.send_keys(subway_station)
        
        station_locator = OrderPageLocators.subway_option(subway_station)
        self.click_element(station_locator)

        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы заказа <Про аренду>")
    def fill_rent_details_form(self, date, rental_period, color, comment):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.rental_period_option(rental_period))

        if color == 'black':
            self.click_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == 'grey':
            self.click_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

        self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить оформление заказа в модальном окне")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_YES_BUTTON)

    @allure.step("Проверить отображение окна успешного оформления заказа")
    def is_success_order_modal_displayed(self):
        return self.find_element(OrderPageLocators.SUCCESS_ORDER_HEADER).is_displayed()
