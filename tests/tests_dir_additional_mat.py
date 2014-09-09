#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirAdditionalMaterials(basetest.BaseTest):

    def test01_add_addit_material(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        ad_mat = constructor_page.navigate_additional_material()
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_nom_element(params_list)
        self.assertTrue(ad_mat.have_nom_element())
        ad_mat.to_update_nom_element()
        self.assertTrue(ad_mat.nom_element_has_params(params_list))
        ad_mat.delete_nom_element()
        self.assertFalse(ad_mat.have_nom_element())

    def test02_add_addit_material(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        ad_mat = constructor_page.navigate_additional_material()
        params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_nom_element(params_list)
        self.assertTrue(ad_mat.have_nom_element())
        ad_mat.to_update_nom_element()
        self.assertTrue(ad_mat.nom_element_has_params(params_list))
        ad_mat.delete_nom_element()
        self.assertFalse(ad_mat.have_nom_element())

    def test03_change_addit_material(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        ad_mat = constructor_page.navigate_additional_material()
        params_list = [
            ["input", ["Вес", "20"]],
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        ad_mat.add_nom_element(params_list)
        self.assertTrue(ad_mat.have_nom_element())
        ad_mat.to_update_nom_element()
        new_params_list = [
            ["input", ["Вес", "50"]],
            ["version", ["Внутренняя"]],
            ["region", ["Европа"]],
        ]
        ad_mat.update_nom_element(new_params_list)
        self.assertTrue(ad_mat.have_nom_element())
        ad_mat.to_update_nom_element()
        self.assertTrue(ad_mat.nom_element_has_params(new_params_list))
        ad_mat.delete_nom_element()
        self.assertFalse(ad_mat.have_nom_element())