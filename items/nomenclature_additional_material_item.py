# coding=utf-8
from __future__ import unicode_literals

from simple_item import SimpleItem
from helpers.waits import *


class NomenclatureAdditionalMaterial(SimpleItem):

    item_type = "nomenclatureAdditionalMaterial"
    element_text = None

    def _update_element_params(self, params_list):
        self.add_info_about_element("NomenclatureAdditionalMaterialProduct")
        self.update_element_params_without_information(params_list)

    def update_element_params_without_information(self, params_list):
        for param in params_list:
            self.do_action(param)
        self.driver.find_element_by_css_selector("#yt1").click()
        wait_until_jquery(self, 5)