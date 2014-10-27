# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *
from helpers.actions_by_label_text import get_input_by_label_text
import random


class Embedded(SimpleItem):

    item_type = "embedded"
    embedded_type = ""
    embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
    title_position = 3

    def choose_kalitka_type(self):
        self.driver.find_element_by_xpath("//span[text()='Калитки']").click()
        wait_until_jquery(self, 5)

    def choose_window_type(self):
        self.driver.find_element_by_xpath("//span[text()='Окна']").click()
        wait_until_jquery(self, 5)

    def choose_type(self, embedded_type):
        if embedded_type == 'kalitka':
            self.choose_kalitka_type()
        elif embedded_type == 'window':
            self.choose_window_type()

    def add_element(self, element_params):
        self.choose_type(self.embedded_type)
        super(Embedded, self).add_element(element_params)

    def _update_element_params(self, element_params):
        self.add_info_about_element("DriverSetProduct")
        self.update_element_params_without_information(element_params)

    def update_element_params_without_information(self, element_params):
        for param in element_params:
            self.do_action(param)
        self.driver.find_element_by_css_selector("#embeddedAdd").click()
        wait_until_jquery(self, 5)

    def add_info_about_element(self, mark):
        self.driver.find_element_by_css_selector("#productField").clear()
        self.driver.find_element_by_css_selector("#productField").send_keys("RSD 02")
        self.driver.find_element_by_xpath("//a[.='RSD 02']").click()

        self.driver.find_element_by_xpath("//a[contains(text(), 'Карты вывода')]").click()
        for_attr = self.driver.find_element_by_xpath("//label[.='Цех']").get_attribute('for')
        self.driver.find_element_by_id(for_attr).click()

    def delete_element(self):
        self.choose_type(self.embedded_type)
        self.driver.find_element_by_css_selector('a.delete').click()
        wait_until_jquery(self, 5)

    def sendkeys_by_label_text(self, label_text, text_to_type):
        element = get_input_by_label_text(self, label_text)
        element.clear()
        element.send_keys(text_to_type)
