# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *


class NomenclatureAdditionalMaterial(SimpleItem):

    item_type = "nomenclatureAdditionalMaterial"
    element_text = None
    product_mark = "NomenclatureAdditionalMaterialProduct"

    def _update_element_params(self, params_list):
        self.add_product()
        self.update_element_params_without_information(params_list)

    def update_element_params_without_information(self, params_list):
        for param in params_list:
            self.do_action(param)
        self.save_element()
        wait_until_jquery(self, 5)

    def element_have_product(self, product_params):
        return super(NomenclatureAdditionalMaterial, self).element_have_product(product_params)

    def save_element(self):
        self.driver.find_element_by_xpath("//a[@id='yt1'] | //a[@id='yt2']").click()

    def add_second_product(self, product_params):
        product_params = ('3', product_params[1], product_params[2])
        self.driver.find_element_by_css_selector('.new-delete #addInputAutoComplete').click()
        self.add_product(product_params)