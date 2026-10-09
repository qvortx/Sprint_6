from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")

    @staticmethod
    def subway_option(station_name):
        return (By.XPATH, f"//div[contains(@class, 'select-search')]//div[text()='{station_name}'] | //div[contains(@class, 'select-search')]//button[contains(., '{station_name}')]")

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    
    @staticmethod
    def rental_period_option(period_text):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{period_text}']")

    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    CONFIRM_ORDER_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
