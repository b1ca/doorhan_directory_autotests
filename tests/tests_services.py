#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsServices(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_service()

    def test01_add_service(self):
        service = self.item
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        service.add_element(params_list)
        self.assertTrue(service.have_element())
        service.to_update_element()
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def test02_add_service(self):
        service = self.item
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service.add_element(params_list)
        self.assertTrue(service.have_element())
        service.to_update_element()
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def test03_change_service(self):
        service = self.item
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service.add_element(params_list)
        self.assertTrue(service.have_element())
        service.to_update_element()
        new_params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["Европа"]],
        ]
        service.update_element_params_without_information(new_params_list)
        self.assertTrue(service.have_element())
        service.to_update_element()
        self.assertTrue(service.element_have_params(new_params_list))
        service.delete_element()
        self.assertFalse(service.have_element())