#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsNomenclatureAdditional(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_nomenclature_additional()

    def _add_simple_nom_addit(self, params_list):
        nom_addit = self.item
        nom_addit.add_element(params_list)
        self.assertTrue(nom_addit.have_element())
        return nom_addit

    def test01_add_nom_element(self):
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        nom_addit = self._add_simple_nom_addit(params_list)
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test02_add_nom_element(self):
        params_list = [
            ["input", ["Вес", "5"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия"]],
        ]
        nom_addit = self._add_simple_nom_addit(params_list)
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test03_change_nom_element(self):
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        nom_addit = self._add_simple_nom_addit(params_list)
        nom_addit.to_update_element()
        new_params_list = [
            ["fx", ["Подходит:", "2"]],
        ]
        nom_addit.update_element_params_without_information(new_params_list)
        self.assertTrue(nom_addit.have_element())
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_params(new_params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test04_add_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit(params_list)
        nom_addit.to_update_element()
        nom_addit.add_second_product(product_params)
        nom_addit._element_have_params(params_list)
        nom_addit.save_element()
        self.assertTrue(nom_addit.have_element())
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_product(product_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def _add_simple_nom_addit_with_2_products(self, params_list, product_params):
        nom_addit = self._add_simple_nom_addit(params_list)
        nom_addit.to_update_element()
        nom_addit.add_second_product(product_params)
        nom_addit._element_have_params(params_list)
        nom_addit.save_element()
        return nom_addit

    def test05_add_dependent_element_to_first_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        nom_addit.to_update_element()
        nom_addit.add_dependent_element(0, dependent_element_params)
        nom_addit.save_element()
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_dependent(dependent_element_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test06_add_dependent_element_to_second_product_as_group_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        nom_addit.to_update_element()
        nom_addit.add_dependent_element(1, dependent_element_params, as_group=True)
        nom_addit.save_element()
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_dependent(dependent_element_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test07_update_second_product_with_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        nom_addit.to_update_element()
        nom_addit.add_dependent_element(1, dependent_element_params)
        nom_addit.save_element()
        nom_addit.to_update_element()
        new_product_params = (1, 'Все изделия', ('Цех', 'Кладовщик'))
        nom_addit.update_second_product(new_product_params)
        nom_addit.save_element()
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_product(new_product_params))
        self.assertTrue(nom_addit.element_have_dependent(dependent_element_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test08_update_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        nom_addit.to_update_element()
        nom_addit.add_dependent_element(1, dependent_element_params)
        nom_addit.save_element()
        new_dependent_element_params = [
            ["fx", ["Количество", "2"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        nom_addit.to_update_element()
        nom_addit.to_update_dependent_element()
        nom_addit.update_dependent_element(new_dependent_element_params)
        nom_addit.save_element()
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_product(product_params))
        self.assertTrue(nom_addit.element_have_dependent(new_dependent_element_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test09_remove_dependent_element(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        dependent_element_params = [
            ["fx", ["Количество", "1"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия", "Европа"]],
        ]
        nom_addit.to_update_element()
        nom_addit.add_dependent_element(0, dependent_element_params)
        nom_addit.save_element()
        nom_addit.to_update_element()
        nom_addit.delete_dependent_element()
        nom_addit.save_element()
        nom_addit.to_update_element()
        self.assertFalse(nom_addit.element_have_dependent(dependent_element_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test10_remove_second_product(self):
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        nom_addit = self._add_simple_nom_addit_with_2_products(params_list, product_params)
        nom_addit.to_update_element()
        nom_addit.delete_second_product()
        nom_addit.to_update_element()
        self.assertFalse(nom_addit.element_have_product(product_params))
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())