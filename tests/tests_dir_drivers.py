#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirDrivers(basetest.BaseTest):

    def test01_add_driver(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr = constructor_page.navigate_driver()
        params_list = [
            ["fx", ["Длина", "10"]],
            ["fx", ["Ширина", "10"]],
            ["fx", ["Упаковочное место", "1"]],
            ["fx", ["Количество", "3"]],

        ]
        dr.add_driver(params_list, "потолочный")
        self.assertTrue(dr.have_driver())
        dr.to_update_driver()
        self.assertTrue(dr.have_driver_type())
        self.assertTrue(dr.have_subdriver())
        dr.delete_driver()
        self.assertFalse(dr.have_driver())

    def test02_add_driver(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr = constructor_page.navigate_driver()
        params_list = [
            ["fx", ["Длина", "20"]],
            ["fx", ["Ширина", "20"]],
            ["fx", ["Упаковочное место", "3"]],
            ["fx", ["Количество", "15"]],

        ]
        dr.add_driver(params_list, "рычажный")
        self.assertTrue(dr.have_driver())
        dr.to_update_driver()
        self.assertTrue(dr.have_driver_type())
        self.assertTrue(dr.have_subdriver())
        dr.delete_driver()
        self.assertFalse(dr.have_driver())

    def test03_add_driver(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr = constructor_page.navigate_driver()
        dr.add_driver([], "потолочный")
        self.assertTrue(dr.have_driver())
        dr.to_update_driver()
        self.assertTrue(dr.have_driver_type())
        self.driver.back()
        dr.delete_driver()
        self.assertFalse(dr.have_driver())

    def test04_change_driver(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        dr = constructor_page.navigate_driver()
        dr.add_driver([], "потолочный")
        self.assertTrue(dr.have_driver())
        dr.to_update_driver()
        dr.choose_driver_type(tpe="рычажный")
        self.assertTrue(dr.have_driver())
        dr.to_update_driver()
        self.assertTrue(dr.have_driver_type())
        self.driver.find_element_by_css_selector("a[href*='/driver/']").click()
        dr.delete_driver()
        self.assertFalse(dr.have_driver())