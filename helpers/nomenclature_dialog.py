# coding=utf-8
from __future__ import unicode_literals
from waits import *
import random


def choose_random_element_from_dict(self):
    el_from_dict_list = self.driver.find_elements_by_xpath(
        "//ul[@class='treeview']//a[not(contains(., '___')) and not(contains(., 'goods for China'))]"
    )
    number_to_click = 0
    el_from_dict_list[number_to_click].click()
    wait_until_jquery(self, 15)

    nomenclature_list = self.driver.find_elements_by_css_selector(".popup-nomenclature-table-container a")
    txt_lst = self.driver.find_elements_by_css_selector(".popup-nomenclature-table-container td:nth-of-type(3)")
    rand_num = random.randrange(0, len(nomenclature_list))
    rand_element = nomenclature_list[rand_num]
    element_text = txt_lst[rand_num].text
    rand_element.click()
    wait_until_jquery(self, 5)
    return element_text