# coding=utf-8
from __future__ import unicode_literals
import random

from base_item import BaseItem
from helpers.nomenclature_dialog import choose_random_element_from_dict
from helpers.waits import *


class Analog(BaseItem):

    item_type = "analog"
    item_name = "test_QWERT_" + str(random.randrange(0, 150))
    item_number = random.randrange(0, 10)

    def add_group(self):
        wait_until_jquery(self, 5)
        self.driver.execute_script("$('#add-"+self.item_type+"-group').dialog('open');")  # open dialog add group
        element_text = self.choose_random_group()
        return element_text

    def choose_random_group(self):
        group_num = random.randrange(0, 10)
        element_text = self.driver.find_elements_by_css_selector("#popupGroups td:nth-of-type(1)")[group_num].text
        self.driver.find_elements_by_css_selector("#popupGroups a")[group_num].click()
        wait_until_jquery(self, 5)
        return element_text

    def add_element(self, element_params, element_name="", selector="a[href$='addElement']"):
        wait_until_jquery(self, 5)
        self.driver.execute_script("$('#dictionary-nomenclature').dialog('open'); return false;")
        element_text = choose_random_element_from_dict(self)
        wait_until_jquery(self, 5)
        return element_text

    def change_item_name(self, old_item_name, new_item_name):
        self.driver.find_element_by_xpath("(//span[text()='"+old_item_name+"']/../..//a)[1]").click()
        wait_until_jquery(self, 5)
        item_name_input = self.driver.find_element_by_css_selector("#%s-title" % self.item_type)
        item_name_input.clear()
        item_name_input.send_keys(new_item_name)
        self.driver.find_element_by_css_selector("#edit-%s-form .submit" % self.item_type).click()
        wait_until_jquery(self, 10)