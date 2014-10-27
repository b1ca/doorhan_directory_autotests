# coding=utf-8
from __future__ import unicode_literals
from base_page import BasePage
from constructor_page import ConstructorPage


class MainPage(BasePage):

    def navigate_cp(self):
        self.driver.find_element_by_css_selector("a[href$='constructor']").click()
        return ConstructorPage(self.driver)