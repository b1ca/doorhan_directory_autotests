# coding=utf-8
from __future__ import unicode_literals
from helpers.nomenclature_dialog import choose_random_element_from_dict

from simple_item import SimpleItem
from helpers.waits import *


class Driver(SimpleItem):

    item_type = "driver"
    driver_type = None
    element_text = None
    additional_element_text = None

    def add_driver(self, additional_element_params_list, driver_type):
        self.driver_type = driver_type
        self.add_element(additional_element_params_list)

    def _update_element_params(self, params_list):
        self.add_info_about_element("NomenclatureDriverElementsProducts")
        self.choose_driver_type()

        self.add_additional_element(params_list)

        self.driver.find_element_by_css_selector("#submitButton").click()
        wait_until_jquery(self, 5)

    def add_additional_element(self, params_list):
        if params_list:
            self.driver.find_element_by_css_selector("#addElementButton").click()
            wait_until_jquery(self, 5)
            self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
            self.additional_element_text = choose_random_element_from_dict(self)
            self.add_info_about_additional_element()
            for param in params_list:
                    self.do_action(param)
            self.driver.find_element_by_css_selector("#submitButtonDriverSet").click()

    def add_info_about_additional_element(self):
        self.add_info_about_element("NomenclatureDriverAdditionalElementsProducts")

    def choose_driver_type(self, driver_type=''):
        xpath_select_with_id = "//select[@id='NomenclatureDriverElementsModel_type_id']"
        if driver_type:
            self.driver_type = driver_type
        self.driver.find_element_by_xpath(xpath_select_with_id+"/option[text()='%s']" % self.driver_type).click()

        if driver_type:
            self.driver.find_element_by_css_selector("#submitButton").click()

    def have_driver_type(self):
        selected_option = self.driver.find_element_by_css_selector(
            "select#NomenclatureDriverElementsModel_type_id option[selected]")
        return selected_option.text == self.driver_type

    def have_additional_element(self):
        additional_element_text = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(3)")[0].text
        self.driver.find_element_by_css_selector("a[href*='/driver/']").click()
        return self.additional_element_text == additional_element_text

    def to_update_additional_element(self):
        self.driver.find_element_by_css_selector("a[title='Update']").click()