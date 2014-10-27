#coding=utf-8
from __future__ import unicode_literals
from basetest import BaseTest
from pages.main_page import MainPage


class TestsColors(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_color()

    def test01_add_color(self):
        color = self.item
        params_list = [
            ["input", ["Цвет", " Фиолетовый"]],
            ["checkbox", ["Для Группы"]],
            ["checkbox", ["Для Щита"]],
        ]
        color.add_element(params_list)
        self.assertTrue(color.have_element())
        color.to_update_element()
        self.assertTrue(color.element_have_params(params_list))
        color.delete_element()
        self.assertFalse(color.have_element())

    def test02_add_color(self):
        color = self.item
        params_list = [
            ["input", ["Цвет", " Зеленый"]],
            ["checkbox", ["Для Щита"]],
        ]
        color.add_element(params_list)
        self.assertTrue(color.have_element())
        color.to_update_element()
        self.assertTrue(color.element_have_params(params_list))
        color.delete_element()
        self.assertFalse(color.have_element())

    def test03_add_color(self):
        color = self.item
        params_list = [
            ["input", ["Цвет", " Красный"]],
            ["checkbox", ["Для Группы"]],
        ]
        color.add_element(params_list)
        self.assertTrue(color.have_element())
        color.to_update_element()
        self.assertTrue(color.element_have_params(params_list))
        color.delete_element()
        self.assertFalse(color.have_element())

    def test04_change_color(self):
        color = self.item
        params_list = [
            ["input", ["Цвет", " Красный"]],
            ["checkbox", ["Для Группы"]],
        ]
        color.add_element(params_list)
        self.assertTrue(color.have_element())
        color.to_update_element()
        new_params_list = [
            ["checkbox", ["Для Щита"]],
        ]
        color.update_element_params_without_information(new_params_list)
        self.assertTrue(color.have_element())
        color.to_update_element()
        self.assertTrue(color.element_have_params(new_params_list))
        color.delete_element()
        self.assertFalse(color.have_element())