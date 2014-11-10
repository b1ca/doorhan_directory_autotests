# coding=utf-8
from __future__ import unicode_literals

import random
import time

from base_item import BaseItem
from simple_item import SimpleItem
from helpers.nomenclature_dialog import choose_random_element_from_dict
from helpers.waits import *


class Group(BaseItem, SimpleItem):

    item_type = "group"
    group_name = 'RH58'
    dependent_element_text = None
    element_text = None

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

    def update_element_params(self, element_params):
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

    def _update_element_params(self, element_params):
        self.update_element_params(element_params)
        self.save_element()

    def save_element(self):
        self.driver.find_element_by_css_selector('a[onclick*="#add-additional-element-form"]').click()

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

    def _add_element(self, element_params):
        wait_until_jquery(self, 10)
        self.driver.find_element_by_css_selector('a[href*=addElement]').click()
        self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
        self.element_text = choose_random_element_from_dict(self)
        self.update_element_params(element_params)

    def add_dependent_element(self, product_count, dep_el_params, as_group=None):
        self.driver.find_element_by_css_selector('#yt0').click()
        self.update_dependent_element(dep_el_params, as_group)

    def update_dependent_element(self, dep_el_params, as_group=None):
        time.sleep(3)
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

    def _update_dependent_element(self, dep_el_params, as_group=None):
        self.update_dependent_element(dep_el_params, as_group)
        self.save_dependent_element()

    def save_dependent_element(self):
        self.driver.find_element_by_xpath("//*[@id='submitButtonDriverSet'] | //*[@id='yt0']").click()

    def add_product(self, product_params=()):
        product_type = 'RSD 02'
        checkbox_maps = ('Цех',)
        if len(product_params) == 3:
            _, product_type, checkbox_maps = product_params
        self.driver.find_element_by_xpath("//input[@id='GroupSubElementModel_product_id']/../button").click()
        self.driver.find_element_by_xpath("//label[.='%s']/input" % product_type).click()
        time.sleep(2)
        self.driver.find_elements_by_css_selector(
            '#GroupSubElementModel_specification_id option:not([selected])')[0].click()
        self.driver.find_elements_by_css_selector('.ui-multiselect')[-1].click()
        time.sleep(1)
        for checkbox_text in checkbox_maps:
            self.driver.find_element_by_xpath("//label[.='%s']/input" % checkbox_text).click()

    def _have_item(self):
        el = self.driver.find_elements_by_xpath("//td[.='%s']" % self.element_text)
        return len(el) == 1

    def to_update_element(self):
        wait_until_jquery(self, 10)
        self.driver.find_element_by_css_selector('a img[src*=update]').click()

    def to_update_dependent_element(self):
        self.driver.find_element_by_css_selector("a[href*='editSubElement']").click()

    def _have_dependent(self):
        el = self.driver.find_elements_by_xpath("//td[.='%s']" % self.dependent_element_text)
        return len(el) == 1

    def delete_dependent_element(self):
        self.driver.find_element_by_css_selector(".delete").click()
        wait_until_jquery(self, 5)
        self.driver.find_element_by_css_selector('.link[title]').click()