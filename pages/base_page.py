from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.base_url = "https://mail.ru/"

	def find_element(self, locator, time = 10):
		return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
														message = f"Can't find element by locator {locator}")

	def find_elements(self, locator, time = 10):
		return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
														message = f"Can't find elements by locator {locator}")

	def check_current_page_by_title(self, text, time = 10):
		title = WebDriverWait(self.driver, time).until(EC.title_is(text),
														message = f"Can't find title with text: {text}")
		assert title

	def load_home_page(self):
		return self.driver.get(self.base_url)
