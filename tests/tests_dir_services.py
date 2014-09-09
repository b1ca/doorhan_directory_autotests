#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirServices(basetest.BaseTest):

    def test01_add_service(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        service = constructor_page.navigate_service()
        params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        service.add_nom_element(params_list)
        self.assertTrue(service.have_nom_element())
        service.to_update_nom_element()
        self.assertTrue(service.nom_element_has_params(params_list))
        service.delete_nom_element()
        self.assertFalse(service.have_nom_element())

    def test02_add_service(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        service = constructor_page.navigate_service()
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service.add_nom_element(params_list)
        self.assertTrue(service.have_nom_element())
        service.to_update_nom_element()
        self.assertTrue(service.nom_element_has_params(params_list))
        service.delete_nom_element()
        self.assertFalse(service.have_nom_element())

    def test03_change_service(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        service = constructor_page.navigate_service()
        params_list = [
            ["version", ["Дилерская"]],
            ["region", ["СНГ"]],
        ]
        service.add_nom_element(params_list)
        self.assertTrue(service.have_nom_element())
        service.to_update_nom_element()
        new_params_list = [
            ["version", ["Внутренняя"]],
            ["region", ["Европа"]],
        ]
        service.update_nom_element(new_params_list)
        self.assertTrue(service.have_nom_element())
        service.to_update_nom_element()
        self.assertTrue(service.nom_element_has_params(new_params_list))
        service.delete_nom_element()
        self.assertFalse(service.have_nom_element())