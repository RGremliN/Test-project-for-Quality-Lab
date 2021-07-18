from .base_page import BasePage
from selenium.webdriver.common.by import By


class LetterPageLocators:
	LOCATOR_FIELD_SEND_TO = (By.XPATH, "//div[contains(@class,'head_container')]//input")
	LOCATOR_FIELD_LETTER_BODY = (By.CSS_SELECTOR, "div[class*='cke_editable_inline '] > div:nth-child(1)")
	LOCATOR_SEND_BTN = (By.CSS_SELECTOR, "div[class='compose-app__footer'] span[class='button2__txt']")
	LOCATOR_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "a[class='layer__link']")


class LetterPage(BasePage):
	def enter_field_send_to(self, send_to):
		send_to_field = self.find_element(LetterPageLocators.LOCATOR_FIELD_SEND_TO)
		send_to_field.click()
		send_to_field.send_keys(send_to)

	def enter_field_body(self, text):
		body_field = self.find_element(LetterPageLocators.LOCATOR_FIELD_LETTER_BODY)
		body_field.click()
		body_field.send_keys(text)

	def click_send_button(self):
		send_button = self.find_element(LetterPageLocators.LOCATOR_SEND_BTN)
		send_button.click()

	def check_success_sent_message(self, text):
		assert self.find_element(LetterPageLocators.LOCATOR_SUCCESS_MESSAGE)
