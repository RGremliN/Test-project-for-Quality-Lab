from .base_page import BasePage
from selenium.webdriver.common.by import By


class EmailsPageLocators:
	LOCATOR_WRITE_MESSAGE_BTN = (By.CLASS_NAME, "compose-button")


class EmailsPage(BasePage):
	def click_write_message_button(self):
		write_message_button = self.find_element(EmailsPageLocators.LOCATOR_WRITE_MESSAGE_BTN)
		write_message_button.click()
