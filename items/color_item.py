# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *


class Color(SimpleItem):

    item_type = "color"
    element_text = None
    title_position = 2
    css_selector_for_add_element_btn = "a[href*='create']"

    def add_element(self, element_params):
        self.driver.find_element_by_css_selector(self.css_selector_for_add_element_btn).click()
        self._update_element_params(element_params)

    def _update_element_params(self, params_list):
        self.update_element_params_without_information(params_list)

    def update_element_params_without_information(self, params_list):
        for param in params_list:
            self.do_action(param)
            if 'input' in param[0] and 'Цвет' in param[1][0]:
                self.element_text = param[1][1]
        self.driver.find_element_by_css_selector("#submitButton").click()
        wait_until_jquery(self, 5)