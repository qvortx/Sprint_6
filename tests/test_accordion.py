import pytest
import allure
from data import Urls, AccordionData
from pages.main_page import MainPage


@allure.suite("Главная страница")
class TestAccordion:

    @allure.title("Проверка выпадающего списка в разделе «Вопросы о важном» для вопроса #{index}")
    @allure.description("Проверяем, что при клике на вопрос раскрывается соответствующий текст ответа.")
    @pytest.mark.parametrize(
        "index, expected_answer",
        AccordionData.ANSWERS.items()
    )
    def test_accordion_answers(self, driver, index, expected_answer):
        main_page = MainPage(driver)

        main_page.open_url(Urls.BASE_URL)
        main_page.accept_cookies()
        main_page.scroll_to_questions_section()
        main_page.click_question(index)

        actual_answer = main_page.get_answer_text(index)
        assert actual_answer == expected_answer
