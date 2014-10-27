#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsDriverSets(BaseTest):
    
    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_driver_set()

    def test01_add_driver_set(self):
        dr_set = self.item
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_element(params_list)
        self.assertTrue(dr_set.have_element())
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test02_add_driver_set(self):
        dr_set = self.item
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_element(params_list)
        self.assertTrue(dr_set.have_element())
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test03_change_driver_set(self):
        dr_set = self.item
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set.add_element(params_list)
        self.assertTrue(dr_set.have_element())
        dr_set.to_update_element()
        new_params_list = [
            ["fx", ["По умолчанию:", "1"]],
        ]
        dr_set.update_element_params_without_information(new_params_list)
        self.assertTrue(dr_set.have_element())
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_params(new_params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())