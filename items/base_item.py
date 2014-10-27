# coding=utf-8
from __future__ import unicode_literals
import time
from helpers.nomenclature_dialog import choose_random_element_from_dict
from helpers.waits import *


class BaseItem(object):
    """
    parent class for - analog, group, shield
    """
    def __init__(self, driver):
        self.driver = driver

    item_type = None
    item = None

    def add_item(self, item_name):
        wait_until_jquery(self, 10)
        self.driver.execute_script("$('#add-%s').dialog('open');" % self.item_type)  # open dialog add item
        add_item_form_input = self.driver.find_element_by_css_selector("#add-%s input" % self.item_type)
        add_item_form_input.send_keys(item_name)
        add_item_save_button = self.driver.find_element_by_css_selector("#add-%s a.submit" % self.item_type)
        add_item_save_button.click()

    def have_item(self, item_name):
        el = self.driver.find_elements_by_xpath("//span[text()='"+item_name+"']")
        return len(el) == 1

    def delete_item(self, item_name):
        delete_btn = self.driver.find_element_by_xpath(
            "//span[text()='%s']/../..//div[@class='group-del']/a" % item_name)
        delete_btn.click()
        self.driver.implicitly_wait(2)
        wait_until_jquery(self, 5)

    def get_number_of_elements(self):
        return len(self.driver.find_elements_by_css_selector(".grid-view tr")) - 1

    def choose_item(self, num_of_item):
        self.driver.find_elements_by_css_selector("div[id^=%s-id]" % self.item_type)[num_of_item].click()
        wait_until_jquery(self, 5)

    def delete_element(self):
        wait_until_jquery(self, 5)
        self.driver.find_elements_by_css_selector("a.delete")[0].click()

    def get_item_name_by_num(self, num_of_item):
        return self.driver.find_elements_by_css_selector("span[class^="+self.item_type+"-title]")[num_of_item].text

    def add_element(self, element_params, element_name="", selector="a[href*='add']"):
        self.driver.find_element_by_css_selector(selector).click()
        self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
        element_text = choose_random_element_from_dict(self)
        self._update_element_params(element_params)
        return element_text

    def _update_element_params(self, element_params):
        raise NotImplementedError

    def have_element(self, element_text, num_of_elements):
        time.sleep(2)
        el_list = self.driver.find_elements_by_css_selector(".grid-view tr td:nth-of-type(3)")
        el_0_text = el_list[0].text
        return el_0_text == element_text and len(el_list) == num_of_elements + 1

    def change_item_name(self, old_item_name, new_item_name):
        self.driver.find_element_by_xpath("(//span[text()='"+old_item_name+"']/../..//a)[1]").click()
        wait_until_jquery(self, 5)
        item_name_input = self.driver.find_element_by_css_selector("#NomenclatureGroupsModelEdit_title")
        item_name_input.clear()
        item_name_input.send_keys(new_item_name)
        self.driver.find_element_by_css_selector("#%s_edit_submit" % self.item_type).click()
        wait_until_jquery(self, 10)