# coding=utf-8
from __future__ import unicode_literals
from selenium.common.exceptions import NoSuchElementException

from simple_item import SimpleItem
from helpers.waits import *
from helpers.actions_by_label_text import get_input_by_label_text
import random


class Embedded(SimpleItem):

    item_type = "embedded"
    embedded_type = ""
    embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
    title_position = 3
    product_mark = ""
    checkbox_maps = None

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
        self.add_product()
        self.update_element_params_without_information(element_params)

    def update_element_params_without_information(self, element_params):
        for param in element_params:
            self.do_action(param)
        self.driver.find_element_by_css_selector("#embeddedAdd").click()
        wait_until_jquery(self, 15)

    def add_product(self, product_params=()):
        product_count = 0
        product_type = 'RSD 02'
        checkbox_maps = ('Цех',)
        if len(product_params) == 3:
            product_count, product_type, checkbox_maps = product_params
        self.checkbox_maps = checkbox_maps
        product = self.driver.find_element_by_css_selector(".product:nth-of-type(%s)" % (product_count+1))
        product.find_element_by_css_selector("#productField").clear()
        product.find_element_by_css_selector("#productField").send_keys(product_type)
        product.find_element_by_xpath("//a[.='%s']" % product_type).click()

        maps_tab = self.driver.find_elements_by_xpath("//a[contains(., 'Карты вывода')]")[-1]
        maps_tab.click()
        wait_until_jquery(self, 5)
        for checkbox_text in checkbox_maps:
            for_attr = self.driver.find_elements_by_xpath("//label[.='%s']" % checkbox_text)[-1].get_attribute('for')
            self.driver.find_element_by_id(for_attr).click()
        wait_until_jquery(self, 25)

    def delete_element(self):
        self.choose_type(self.embedded_type)
        self.driver.find_element_by_css_selector('a.delete').click()
        wait_until_jquery(self, 5)

    def sendkeys_by_label_text(self, label_text, text_to_type):
        element = get_input_by_label_text(self, label_text)
        element.clear()
        element.send_keys(text_to_type)

    def add_second_product(self, product_params):
        self.driver.find_element_by_css_selector("#addProductBlockButton").click()
        wait_until_jquery(self, 5)
        self.add_product(product_params)

    def save_element(self):
        self.driver.find_element_by_css_selector('#embeddedAdd').click()

    def element_have_product(self, product_params):
        self.driver.implicitly_wait(2)
        product_count, product_type, checkbox_maps = product_params
        try:
            product = self.driver.find_element_by_css_selector(".product:nth-of-type(%s)" % (product_count+1))
            product_field_result = product.find_element_by_css_selector(
                ".autocompleteProducts").get_attribute("value") == product_type
            checkbox_maps_result = []
            maps_tab = self.driver.find_elements_by_xpath("//a[contains(., 'Карты вывода')]")[-1]
            maps_tab.click()
            wait_until_jquery(self, 5)
            for checkbox_text in checkbox_maps:
                for_attr = self.driver.find_elements_by_xpath(
                    "//label[.='%s']" % checkbox_text)[-1].get_attribute('for')
                checkbox_maps_result.append(self.driver.find_element_by_id(for_attr).is_selected())
            checkbox_maps_result = all(checkbox_maps_result)
            return all([product_field_result, checkbox_maps_result])
        except (IndexError, NoSuchElementException) as e:
            print e.message
            return False

    def update_product(self, new_product_params):
        if not len(new_product_params) == 3:
            raise Exception('product params must be tuple or list of 3 elements.')
        checkbox_maps = self.checkbox_maps
        maps_tab = self.driver.find_elements_by_xpath("//a[contains(., 'Карты вывода')]")[-1]
        maps_tab.click()
        wait_until_jquery(self, 5)
        for checkbox_text in checkbox_maps:
            for_attr = self.driver.find_elements_by_xpath("//label[.='%s']" % checkbox_text)[-1].get_attribute('for')
            self.driver.find_element_by_id(for_attr).click()
        self.add_product(new_product_params)

    def delete_product(self, product_count):
        self.driver.find_elements_by_css_selector('#deleteProductBlockButton')[product_count].click()