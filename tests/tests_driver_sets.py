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

    def _add_simple_driver_set(self, params_list):
        dr_set = self.item
        dr_set.add_element(params_list)
        self.assertTrue(dr_set.have_element())
        return dr_set

    def test01_add_driver_set(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        dr_set = self._add_simple_driver_set(params_list)
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test02_add_driver_set(self):
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set = self._add_simple_driver_set(params_list)
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test03_change_driver_set(self):
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        dr_set = self._add_simple_driver_set(params_list)
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

    def test04_add_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set(params_list)
        dr_set.to_update_element()
        dr_set.add_second_product(product_params)
        dr_set._element_have_params(params_list)
        dr_set.save_element()
        self.assertTrue(dr_set.have_element())
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_product(product_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def _add_simple_driver_set_with_2_products(self, params_list, product_params):
        dr_set = self._add_simple_driver_set(params_list)
        dr_set.to_update_element()
        dr_set.add_second_product(product_params)
        dr_set._element_have_params(params_list)
        dr_set.save_element()
        return dr_set

    def test05_add_dependent_element_to_first_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        dr_set.to_update_element()
        dr_set.add_dependent_element(0, dependent_element_params)
        dr_set.save_element()
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_dependent(dependent_element_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test06_add_dependent_element_to_second_product_as_group_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        dr_set.to_update_element()
        dr_set.add_dependent_element(1, dependent_element_params, as_group=True)
        dr_set.save_element()
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_dependent(dependent_element_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test07_update_second_product_with_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        dr_set.to_update_element()
        dr_set.add_dependent_element(1, dependent_element_params)
        dr_set.save_element()
        dr_set.to_update_element()
        new_product_params = (1, 'Все изделия', ('Цех', 'Кладовщик'))
        dr_set.update_second_product(new_product_params)
        dr_set.save_element()
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_product(new_product_params))
        self.assertTrue(dr_set.element_have_dependent(dependent_element_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test08_update_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        dr_set.to_update_element()
        dr_set.add_dependent_element(1, dependent_element_params)
        dr_set.save_element()
        new_dependent_element_params = [
            ["fx", ["Количество", "2"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        dr_set.to_update_element()
        dr_set.to_update_dependent_element()
        dr_set.update_dependent_element(new_dependent_element_params)
        dr_set.save_element()
        dr_set.to_update_element()
        self.assertTrue(dr_set.element_have_product(product_params))
        self.assertTrue(dr_set.element_have_dependent(new_dependent_element_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test09_remove_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        dr_set.to_update_element()
        dr_set.add_dependent_element(0, dependent_element_params)
        dr_set.save_element()
        dr_set.to_update_element()
        dr_set.delete_dependent_element()
        dr_set.save_element()
        dr_set.to_update_element()
        self.assertFalse(dr_set.element_have_dependent(dependent_element_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())

    def test10_remove_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        dr_set = self._add_simple_driver_set_with_2_products(params_list, product_params)
        dr_set.to_update_element()
        dr_set.delete_second_product()
        dr_set.to_update_element()
        self.assertFalse(dr_set.element_have_product(product_params))
        self.assertTrue(dr_set.element_have_params(params_list))
        dr_set.delete_element()
        self.assertFalse(dr_set.have_element())