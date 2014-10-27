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

    def test01_add_nom_element(self):
        nom_addit = self.item
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        nom_addit.add_element(params_list)
        self.assertTrue(nom_addit.have_element())
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test02_add_nom_element(self):
        nom_addit = self.item
        params_list = [
            ["input", ["Вес", "5"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["version", ["Дилерская"]],
            ["region", ["Азия"]],
        ]
        nom_addit.add_element(params_list)
        self.assertTrue(nom_addit.have_element())
        nom_addit.to_update_element()
        self.assertTrue(nom_addit.element_have_params(params_list))
        nom_addit.delete_element()
        self.assertFalse(nom_addit.have_element())

    def test03_change_nom_element(self):
        nom_addit = self.item
        params_list = [
            ["input", ["Вес", "20"]],
            ["checkbox", ["Участвует в расчете веса щита"]],
            ["fx", ["Подходит:", "1"]],
            ["fx", ["По умолчанию:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        nom_addit.add_element(params_list)
        self.assertTrue(nom_addit.have_element())
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