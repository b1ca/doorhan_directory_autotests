#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsDrivers(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_driver()

    def test01_add_driver_with_additional_element(self):
        dr = self.item
        additional_element_params_list = [
            ["fx", ["Длина", "10"]],
            ["fx", ["Ширина", "10"]],
            ["fx", ["Упаковочное место", "1"]],
            ["fx", ["Количество", "3"]],
        ]
        dr.add_driver(additional_element_params_list, driver_type="потолочный")
        self.assertTrue(dr.have_element())
        dr.to_update_element()
        self.assertTrue(dr.have_driver_type())
        self.assertTrue(dr.have_additional_element())
        dr.delete_element()
        self.assertFalse(dr.have_element())

    def test02_add_driver_with_additional_element(self):
        dr = self.item
        additional_element_params_list = [
            ["fx", ["Длина", "20"]],
            ["fx", ["Ширина", "20"]],
            ["fx", ["Упаковочное место", "3"]],
            ["fx", ["Количество", "15"]],
        ]
        dr.add_driver(additional_element_params_list, driver_type="рычажный")
        self.assertTrue(dr.have_element())
        dr.to_update_element()
        self.assertTrue(dr.have_driver_type())
        self.assertTrue(dr.have_additional_element())
        dr.delete_element()
        self.assertFalse(dr.have_element())

    def test03_add_driver(self):
        dr = self.item
        dr.add_driver([], driver_type="потолочный")
        self.assertTrue(dr.have_element())
        dr.to_update_element()
        self.assertTrue(dr.have_driver_type())
        self.driver.back()
        dr.delete_element()
        self.assertFalse(dr.have_element())

    def test04_change_driver(self):
        dr = self.item
        dr.add_driver([], driver_type="потолочный")
        self.assertTrue(dr.have_element())
        dr.to_update_element()
        dr.choose_driver_type(driver_type="рычажный")
        self.assertTrue(dr.have_element())
        dr.to_update_element()
        self.assertTrue(dr.have_driver_type())
        self.driver.find_element_by_css_selector("a[href*='/driver/']").click()
        dr.delete_element()
        self.assertFalse(dr.have_element())