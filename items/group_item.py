# coding=utf-8
from __future__ import unicode_literals

import random

from base_item import BaseItem
from helpers.waits import *


class Group(BaseItem):

    item_type = "group"

    def change_element_params(self, element_to_change, element_params):
        self.driver.find_elements_by_css_selector('td.button-column a[href*="edit"]')[element_to_change].click()
        old_color = self._get_element_color()
        self._update_element_params(element_params)
        return old_color

    def element_has_params(self, element_number, element_params):
        import time
        time.sleep(3)
        self.driver.find_elements_by_css_selector('td.button-column a[href*="edit"]')[element_number].click()
        if element_params["color"]:
            color_field = self.driver.find_element_by_css_selector("#NomenclatureGroupElementsModel_color_val")
            return element_params["color"].lower() in color_field.get_attribute("value").lower()

    def _get_element_color(self):
        return self.driver.find_element_by_css_selector(
            "#NomenclatureGroupElementsModel_color_val").get_attribute('value')

    def _update_element_params(self, element_params):
        if element_params:
            if element_params["color"]:
                color_field = self.driver.find_element_by_css_selector("#NomenclatureGroupElementsModel_color_val")
                color_field.clear()
                color_field.send_keys(element_params["color"])
                wait_until_jquery(self, 5)
                if len(self.driver.find_elements_by_css_selector(".ui-menu-item a")) > 0:
                    self.driver.find_element_by_css_selector(".ui-menu-item a").click()
            if element_params["Версия"]:
                self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
                for version in element_params["Версия"]:
                    self.driver.find_element_by_xpath("//label[contains(text(), '%s')]" % version).click()
            if element_params["Регион"]:
                self.driver.find_elements_by_xpath("//a[contains(text(), 'Регион')]")[0].click()
                for region in element_params["Регион"]:
                    self.driver.find_element_by_xpath(
                        "//*[@class='daredevel-tree-label'][text()='%s']/../input" % region).click()
        self.driver.execute_script("$('#add-additional-element-form').submit();")

    def have_item(self, item_name):
        el = self.driver.find_elements_by_xpath("//span[text()='"+item_name+"']")
        return len(el) == 1

    def delete_item(self, item_name):
        delete_btn = self.driver.find_element_by_xpath(
            "//span[text()='%s']/../..//div[@class='group-del']/a" % item_name)
        delete_btn.click()
        self.driver.find_element_by_css_selector('a[onclick*="remove"]').click()
        self.driver.implicitly_wait(2)
        wait_until_jquery(self, 5)

    def add_group_with_params(self, params_dict):
        num_of_group = random.randrange(0, 10)
        self.choose_item(num_of_group)
        num_of_elements = self.get_number_of_elements()
        element_text = self.add_element(params_dict)
        assert self.have_element(element_text, num_of_elements)
        self.delete_element()
        self.choose_item(num_of_group)
        assert not self.have_element(element_text, num_of_elements)