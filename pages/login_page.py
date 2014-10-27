# coding=utf-8
from __future__ import unicode_literals
from base_page import BasePage
from main_page import MainPage


class LoginPage(BasePage):

    def do_login(self, login, password):
        self.driver.find_element_by_css_selector("#LoginForm_username").send_keys(login)
        self.driver.find_element_by_css_selector("#LoginForm_password").send_keys(password)
        self.driver.find_element_by_css_selector("input[type=submit]").click()
        return MainPage(self.driver)