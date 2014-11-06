# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *


class NomenclatureAdditional(SimpleItem):

    item_type = "nomenclatureAdditional"
    element_text = None
    product_mark = "NomenclatureAdditionalProduct"
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