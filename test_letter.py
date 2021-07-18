from auth_data import AuthData
from pages.main_page import MainPage
from pages.emails_page import EmailsPage
from pages.letter_page import LetterPage

import time


def test_send_letter(browser_chrome):
	mainPage = MainPage(browser_chrome)
	mainPage.load_home_page()
	mainPage.check_current_page_by_title("Mail.ru: почта, поиск в интернете, новости, игры")
	mainPage.log_in(username = AuthData.username, password = AuthData.password)

	emailPage = EmailsPage(browser_chrome)
	emailPage.check_current_page_by_title("Входящие - Почта Mail.ru")
	emailPage.click_write_message_button()

	letterPage = LetterPage(browser_chrome)
	letterPage.enter_field_send_to(AuthData.username)
	letterPage.enter_field_body(AuthData.username)
	letterPage.click_send_button()
	letterPage.check_success_sent_message("Письмо отправлено")

