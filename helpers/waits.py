from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def wait_until_jquery(self, seconds_to_wait):
    jquery_active = lambda x: self.driver.execute_script("return jQuery.active == 0")
    WebDriverWait(self.driver, seconds_to_wait).until(jquery_active)


def wait_until_jquery_is_ready(self, seconds_to_wait):
    jquery_is_ready = lambda x: self.driver.execute_script("return jQuery.isReady == true")
    WebDriverWait(self.driver, seconds_to_wait).until(jquery_is_ready)


def wait_until_ui_dialog(self, seconds_to_wait):
    WebDriverWait(self.driver, seconds_to_wait).\
        until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog")))


def wait_until_title_is_equal(self, seconds_to_wait, title):
    WebDriverWait(self.driver, seconds_to_wait).\
        until(ec.title_is(title))


def wait_until_text_present(self, seconds_to_wait, locator, text):
    WebDriverWait(self.driver, seconds_to_wait).until(ec.text_to_be_present_in_element(locator, text))