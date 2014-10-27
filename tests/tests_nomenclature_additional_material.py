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

    def test01_add_addit_material(self):
        ad_mat = self.item
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_element(params_list)
        self.assertTrue(ad_mat.have_element())
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def test02_add_addit_material(self):
        ad_mat = self.item
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_element(params_list)
        self.assertTrue(ad_mat.have_element())
        ad_mat.to_update_element()
        self.assertTrue(ad_mat.element_have_params(params_list))
        ad_mat.delete_element()
        self.assertFalse(ad_mat.have_element())

    def test03_change_addit_material(self):
        ad_mat = self.item
        params_list = [
            ["input", ["Вес", "20"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_element(params_list)
        self.assertTrue(ad_mat.have_element())
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