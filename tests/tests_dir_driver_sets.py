#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirDriverSets(basetest.BaseTest):

    def test01_add_driver_set(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr_set = constructor_page.navigate_driver_set()
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_nom_element(params_list)
        self.assertTrue(dr_set.have_nom_element())
        dr_set.to_update_nom_element()
        self.assertTrue(dr_set.nom_element_has_params(params_list))
        dr_set.delete_nom_element()
        self.assertFalse(dr_set.have_nom_element())

    def test02_add_driver_set(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr_set = constructor_page.navigate_driver_set()
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_nom_element(params_list)
        self.assertTrue(dr_set.have_nom_element())
        dr_set.to_update_nom_element()
        self.assertTrue(dr_set.nom_element_has_params(params_list))
        dr_set.delete_nom_element()
        self.assertFalse(dr_set.have_nom_element())

    def test03_change_driver_set(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr_set = constructor_page.navigate_driver_set()
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_nom_element(params_list)
        self.assertTrue(dr_set.have_nom_element())
        dr_set.to_update_nom_element()
        new_params_list = [
            ["fx", ["По умолчанию:", "1"]],
        ]
        dr_set.update_nom_element(new_params_list)
        self.assertTrue(dr_set.have_nom_element())
        dr_set.to_update_nom_element()
        self.assertTrue(dr_set.nom_element_has_params(new_params_list))
        dr_set.delete_nom_element()
        self.assertFalse(dr_set.have_nom_element())