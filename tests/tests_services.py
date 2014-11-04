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

    def _add_simple_service(self, params_list):
        service = self.item
        service.add_element(params_list)
        self.assertTrue(service.have_element())
        return service

    def test01_add_service(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        service = self._add_simple_service(params_list)
        service.to_update_element()
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def test02_add_service(self):
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service = self._add_simple_service(params_list)
        service.to_update_element()
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def test03_change_service(self):
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service = self._add_simple_service(params_list)
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

    def test04_add_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        service = self._add_simple_service(params_list)
        service.to_update_element()
        service.add_second_product(product_params)
        service._element_have_params(params_list)
        service.save_element()
        self.assertTrue(service.have_element())
        service.to_update_element()
        self.assertTrue(service.element_have_product(product_params))
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def _add_simple_service_with_2_products(self, params_list, product_params):
        service = self._add_simple_service(params_list)
        service.to_update_element()
        service.add_second_product(product_params)
        service._element_have_params(params_list)
        service.save_element()
        return service

    def test05_update_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        service = self._add_simple_service_with_2_products(params_list, product_params)
        service.to_update_element()
        new_product_params = (1, 'Все изделия', ('Цех', 'Кладовщик'))
        service.update_second_product(new_product_params)
        service.save_element()
        service.to_update_element()
        self.assertTrue(service.element_have_product(new_product_params))
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())

    def test06_delete_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        service = self._add_simple_service_with_2_products(params_list, product_params)
        service.to_update_element()
        service.delete_second_product()
        service.to_update_element()
        self.assertFalse(service.element_have_product(product_params))
        self.assertTrue(service.element_have_params(params_list))
        service.delete_element()
        self.assertFalse(service.have_element())