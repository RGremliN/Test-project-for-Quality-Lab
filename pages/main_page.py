from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
	LOCATOR_USERNAME_FIELD = (By.NAME, "login")
	LOCATOR_PASSWD_FIELD = (By.NAME, "password")
	LOCATOR_PASSWD_BTN = (By.XPATH, "//button[@data-testid='enter-password']")
	LOCATOR_LOGIN_BTN = (By.XPATH, "//button[@data-testid='login-to-mail']")


class MainPage(BasePage):
	def enter_login(self, login):
		username_field = self.find_element(MainPageLocators.LOCATOR_USERNAME_FIELD)
		username_field.click()
		username_field.send_keys(login)

	def enter_password(self, password):
		password_field = self.find_element(MainPageLocators.LOCATOR_PASSWD_FIELD)
		password_field.click()
		password_field.send_keys(password)

	def click_enter_password_button(self):
		password_enter_button = self.find_element(MainPageLocators.LOCATOR_PASSWD_BTN)
		password_enter_button.click()

	def click_login_button(self):
		login_button = self.find_element(MainPageLocators.LOCATOR_LOGIN_BTN)
		login_button.click()

	def log_in(self, username='', password=''):
		self.enter_login(username)
		self.click_enter_password_button()
		self.enter_password(password)
		self.click_login_button()
