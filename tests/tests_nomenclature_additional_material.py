#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsNomenclatureAdditionalMaterials(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_nomenclature_additional_material()

    def _add_simple_addit_material(self, params_list):
        ad_mat = self.item
        ad_mat.add_element(params_list)
        self.assertTrue(ad_mat.have_element())
        return ad_mat

    def test01_add_addit_material(self):
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        ad_mat = self._add_simple_addit_material(params_list)
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def test02_add_addit_material(self):
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat = self._add_simple_addit_material(params_list)
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def test03_change_addit_material(self):
        params_list = [
            ["input", ["Вес", "20"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat = self._add_simple_addit_material(params_list)
        ad_mat.to_update_element()
        new_params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["Европа"]],
        ]
        ad_mat.update_element_params_without_information(new_params_list)
        self.assertTrue(ad_mat.have_element())
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_params(new_params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())
        
    def test04_add_second_product(self):
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        ad_mat = self._add_simple_addit_material(params_list)
        ad_mat.to_update_element()
        ad_mat.add_second_product(product_params)
        ad_mat._element_have_params(params_list)
        ad_mat.save_element()
        self.assertTrue(ad_mat.have_element())
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_product(product_params))
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def _add_simple_addit_material_with_2_products(self, params_list, product_params):
        ad_mat = self._add_simple_addit_material(params_list)
        ad_mat.to_update_element()
        ad_mat.add_second_product(product_params)
        ad_mat._element_have_params(params_list)
        ad_mat.save_element()
        return ad_mat

    def test05_update_second_product(self):
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        ad_mat = self._add_simple_addit_material_with_2_products(params_list, product_params)
        ad_mat.to_update_element()
        new_product_params = (1, 'Все изделия', ('Цех', 'Кладовщик'))
        ad_mat.update_second_product(new_product_params)
        ad_mat.save_element()
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_product(new_product_params))
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def test06_delete_second_product(self):
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        product_params = (1, 'RSD 01', ('Цех', 'Кладовщик', 'Мастер'))
        ad_mat = self._add_simple_addit_material_with_2_products(params_list, product_params)
        ad_mat.to_update_element()
        ad_mat.delete_second_product()
        ad_mat.to_update_element()
        self.assertFalse(ad_mat.element_have_product(product_params))
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())