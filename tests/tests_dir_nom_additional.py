#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirNomAdditional(basetest.BaseTest):

    #TODO баг дурхана

    def test01_add_nom_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        addit_nom = constructor_page.navigate_nomenclature_additional()
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        addit_nom.add_nom_element(params_list)
        self.assertTrue(addit_nom.have_nom_element())
        addit_nom.to_update_nom_element()
        self.assertTrue(addit_nom.nom_element_has_params(params_list))
        addit_nom.delete_nom_element()
        self.assertFalse(addit_nom.have_nom_element())

    def test02_add_nom_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        addit_nom = constructor_page.navigate_nomenclature_additional()
        params_list = [
            ["input", ["Вес", "5"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия"]],
        ]
        addit_nom.add_nom_element(params_list)
        self.assertTrue(addit_nom.have_nom_element())
        addit_nom.to_update_nom_element()
        self.assertTrue(addit_nom.nom_element_has_params(params_list))
        addit_nom.delete_nom_element()
        self.assertFalse(addit_nom.have_nom_element())

    def test03_change_nom_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        addit_nom = constructor_page.navigate_nomenclature_additional()
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        addit_nom.add_nom_element(params_list)
        self.assertTrue(addit_nom.have_nom_element())
        addit_nom.to_update_nom_element()
        new_params_list = [
            ["fx", ["Подходит:", "2"]],
        ]
        addit_nom.update_nom_element(new_params_list)
        self.assertTrue(addit_nom.have_nom_element())
        addit_nom.to_update_nom_element()
        self.assertTrue(addit_nom.nom_element_has_params(new_params_list))
        addit_nom.delete_nom_element()
        self.assertFalse(addit_nom.have_nom_element())