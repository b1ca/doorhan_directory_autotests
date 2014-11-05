# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *
from helpers.nomenclature_dialog import choose_random_element_from_dict


class DriverSet(SimpleItem):

    item_type = "driverSet"
    element_text = None
    product_mark = "DriverSetProduct"
    dependent_element_text = None
    product_count = None
    group_name = 'RH58'

    def _update_element_params(self, params_list):
        self.add_product()
        self.update_element_params_without_information(params_list)

    def update_element_params_without_information(self, params_list):
        for param in params_list:
            self.do_action(param)
        self.save_element()
        wait_until_jquery(self, 5)

    def save_element(self):
        self.driver.find_element_by_xpath(
            "//a[@id='yt4'][.='Сохранить'] | //a[@id='yt2'][.='Добавить'] | //a[@id='yt2'][.='Сохранить']").click()

    def add_dependent_element(self, product_count, dep_el_params, as_group=None):
        self.product_count = product_count
        self.driver.find_element_by_css_selector(".products[count='%s'] a[id*='yt']" % product_count).click()
        if as_group:
            self.driver.find_element_by_css_selector("input[value='group']").click()
            group_input = self.driver.find_element_by_css_selector("#autocompleteGroups")
            group_input.click()
            group_input.clear()
            group_input.send_keys(self.group_name)
            self.driver.find_element_by_xpath("//a[.='%s']" % self.group_name).click()
            self.dependent_element_text = self.group_name
        else:
            self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
            self.dependent_element_text = choose_random_element_from_dict(self)
        for param in dep_el_params:
            self.do_action(param)
        self.save_dependent_element()

    def save_dependent_element(self):
        self.driver.find_element_by_css_selector("#yt0").click()

    def to_update_dependent_element(self):
        self.driver.find_element_by_css_selector("a[href*='editDependElement']").click()

    def element_have_dependent(self, dependent_element_params):
        assert self.dependent_element_text in self.driver.find_element_by_css_selector(
            ".products[count='%s']" % self.product_count).text
        self.to_update_dependent_element()
        result = all(self.check_params_on_page(param) for param in dependent_element_params)
        self.driver.find_element_by_css_selector(".btn-white a").click()
        return result