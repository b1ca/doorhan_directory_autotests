#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest


class TestDirColors(basetest.BaseTest):

    def test01_add_color(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        color = constructor_page.navigate_color()
        params_list = [
            ["input", ["Цвет", " Фиолетовый"]],
            ["checkbox", ["Для Группы"]],
            ["checkbox", ["Для Щита"]],
        ]
        color.add_color_element(params_list)
        self.assertTrue(color.have_color_element())
        color.to_update_color_element()
        self.assertTrue(color.color_element_has_params(params_list))
        color.delete_color_element()
        self.assertFalse(color.have_color_element())

    def test02_add_color(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        color = constructor_page.navigate_color()
        params_list = [
            ["input", ["Цвет", " Зеленый"]],
            ["checkbox", ["Для Щита"]],
        ]
        color.add_color_element(params_list)
        self.assertTrue(color.have_color_element())
        color.to_update_color_element()
        self.assertTrue(color.color_element_has_params(params_list))
        color.delete_color_element()
        self.assertFalse(color.have_color_element())

    def test03_add_color(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        color = constructor_page.navigate_color()
        params_list = [
            ["input", ["Цвет", " Красный"]],
            ["checkbox", ["Для Группы"]],
        ]
        color.add_color_element(params_list)
        self.assertTrue(color.have_color_element())
        color.to_update_color_element()
        self.assertTrue(color.color_element_has_params(params_list))
        color.delete_color_element()
        self.assertFalse(color.have_color_element())

    def test04_change_color(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        color = constructor_page.navigate_color()
        params_list = [
            ["input", ["Цвет", " Красный"]],
            ["checkbox", ["Для Группы"]],
        ]
        color.add_color_element(params_list)
        self.assertTrue(color.have_color_element())
        color.to_update_color_element()
        new_params_list = [
            ["checkbox", ["Для Щита"]],
        ]
        color.update_color_element(new_params_list)
        self.assertTrue(color.have_color_element())
        color.to_update_color_element()
        self.assertTrue(color.color_element_has_params(new_params_list))
        color.delete_color_element()
        self.assertFalse(color.have_color_element())