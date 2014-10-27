#coding=utf-8
from __future__ import unicode_literals

from basetest import BaseTest
from pages.main_page import MainPage


class TestsEmbedded(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_embedded()

    def test01_add_kalitka_element(self):
        embedded = self.item
        embedded.embedded_type = 'kalitka'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["fx", ["Минимальная ширина", "0"]],
            ["fx", ["Ширина по умолчанию", "5"]],
            ["fx", ["Максимальная ширина", "50"]],
            ["fx", ["Минимальная высота", "3"]],
            ["fx", ["Высота по умолчанию", "10"]],
            ["option", ["Тип", "Калитка v5"]],
            ["radio", ["Встроенный", "Нет"]],
            ["fx", ["Дистанция до объекта", "15"]],
            ["radio", ["Расположение петель", "только справа"]],
            ["radio", ["Комплект антипаника", "нет"]],
            ["radio", ["Цвет окантовки", "Только 8014"]],
            ["radio", ["Открытие калитки", "Только наружу"]],
            ["radio", ["Выдать доводчик открытой калитки", "нет"]],
            ["radio", ["Выдавать глазок", "да"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test02_add_kalitka_element(self):
        embedded = self.item
        embedded.embedded_type = 'kalitka'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["fx", ["Минимальная ширина", "1"]],
            ["fx", ["Ширина по умолчанию", "3"]],
            ["fx", ["Максимальная ширина", "20"]],
            ["fx", ["Минимальная высота", "1"]],
            ["fx", ["Высота по умолчанию", "5"]],
            ["option", ["Тип", "Калитка v3"]],
            ["radio", ["Встроенный", "Да"]],
            ["fx", ["Дистанция до объекта", "10"]],
            ["radio", ["Расположение петель", "только слева"]],
            ["radio", ["Комплект антипаника", "да"]],
            ["radio", ["Цвет окантовки", "Только Металлик"]],
            ["radio", ["Открытие калитки", "Только наружу"]],
            ["radio", ["Выдать доводчик открытой калитки", "нет"]],
            ["radio", ["Выдавать глазок", "нет"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test03_add_kalitka_element(self):
        embedded = self.item
        embedded.embedded_type = 'kalitka'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["fx", ["Минимальная ширина", "0"]],
            ["fx", ["Ширина по умолчанию", "5"]],
            ["fx", ["Максимальная ширина", "50"]],
            ["fx", ["Минимальная высота", "3"]],
            ["fx", ["Высота по умолчанию", "10"]],
            ["option", ["Тип", "Калитка v2"]],
            ["radio", ["Встроенный", "Нет"]],
            ["fx", ["Дистанция до объекта", "15"]],
            ["fx", ["Слева", "5", 0]],
            ["fx", ["Сверху", "5", 0]],
            ["fx", ["Справа", "5", 0]],
            ["fx", ["Снизу", "5", 0]],
            ["fx", ["Слева", "5", 1]],
            ["fx", ["Сверху", "5", 1]],
            ["fx", ["Справа", "5", 1]],
            ["fx", ["Снизу", "5", 1]],
            ["radio", ["Расположение петель", "только справа"]],
            ["radio", ["Комплект антипаника", "нет"]],
            ["radio", ["Цвет окантовки", "Только RAL9003"]],
            ["radio", ["Открытие калитки", "Только наружу"]],
            ["radio", ["Выдать доводчик открытой калитки", "нет"]],
            ["radio", ["Выдавать глазок", "да"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test04_add_window_element(self):
        embedded = self.item
        embedded.embedded_type = 'window'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["checkbox", ["Круглое"]],
            ["input", ["Радиус", "10"]],
            ["input", ["Артикул", "8"]],
            ["input", ["Вес", "15"]],
            ["fx", ["Ширина по умолчанию", "10"]],
            ["fx", ["Высота по умолчанию", "10"]],
            ["fx", ["Размер фрезерования окна по ширине", "1"]],
            ["fx", ["Размер фрезерования окна по высоте", "1"]],
            ["radio", ["Встроенный", "Да"]],
            ["fx", ["Дистанция до объекта", "15"]],
            ["fx", ["Слева", "5"]],
            ["fx", ["Сверху", "5"]],
            ["fx", ["Справа", "5"]],
            ["fx", ["Снизу", "5"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test05_add_window_element(self):
        embedded = self.item
        embedded.embedded_type = 'window'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["checkbox", ["Круглое"]],
            ["input", ["Радиус", "25"]],
            ["input", ["Артикул", "10"]],
            ["input", ["Вес", "20"]],
            ["fx", ["Ширина по умолчанию", "1"]],
            ["fx", ["Высота по умолчанию", "2"]],
            ["fx", ["Размер фрезерования окна по ширине", "1"]],
            ["fx", ["Размер фрезерования окна по высоте", "1"]],
            ["radio", ["Встроенный", "Нет"]],
            ["fx", ["Дистанция до объекта", "15"]],
            ["fx", ["Слева", "1"]],
            ["fx", ["Сверху", "2"]],
            ["fx", ["Справа", "3"]],
            ["fx", ["Снизу", "4"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test06_change_kalitka_element(self):
        embedded = self.item
        embedded.embedded_type = 'kalitka'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["fx", ["Минимальная ширина", "1"]],
            ["fx", ["Ширина по умолчанию", "3"]],
            ["fx", ["Максимальная ширина", "20"]],
            ["fx", ["Минимальная высота", "1"]],
            ["fx", ["Высота по умолчанию", "5"]],
            ["option", ["Тип", "Калитка v3"]],
            ["radio", ["Встроенный", "Да"]],
            ["fx", ["Дистанция до объекта", "10"]],
            ["radio", ["Расположение петель", "только слева"]],
            ["radio", ["Комплект антипаника", "да"]],
            ["radio", ["Цвет окантовки", "Только Металлик"]],
            ["radio", ["Открытие калитки", "Только наружу"]],
            ["radio", ["Выдать доводчик открытой калитки", "нет"]],
            ["radio", ["Выдавать глазок", "нет"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        new_params_list = [
            ["fx", ["Слева", "10"]],
            ["fx", ["Сверху", "15"]],
            ["fx", ["Справа", "20"]],
            ["fx", ["Снизу", "25"]],
        ]
        embedded.update_element_params_without_information(new_params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(new_params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())

    def test07_change_window_element(self):
        embedded = self.item
        embedded.embedded_type = 'window'
        params_list = [
            ["input", ["Название", embedded.embedded_name]],
            ["checkbox", ["Круглое"]],
            ["input", ["Радиус", "25"]],
            ["input", ["Артикул", "10"]],
            ["input", ["Вес", "20"]],
            ["fx", ["Ширина по умолчанию", "1"]],
            ["fx", ["Высота по умолчанию", "2"]],
            ["fx", ["Размер фрезерования окна по ширине", "1"]],
            ["fx", ["Размер фрезерования окна по высоте", "1"]],
            ["radio", ["Встроенный", "Нет"]],
            ["fx", ["Дистанция до объекта", "15"]],
            ["fx", ["Слева", "1"]],
            ["fx", ["Сверху", "2"]],
            ["fx", ["Справа", "3"]],
            ["fx", ["Снизу", "4"]],
        ]
        embedded.add_element(params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        new_params_list = [
            ["input", ["Название", "TEMP_NAME"]],
            ["input", ["Радиус", "30"]],
            ["input", ["Артикул", "30"]],
            ["input", ["Вес", "30"]],
        ]
        embedded.update_element_params_without_information(new_params_list)
        self.assertTrue(embedded.have_element())
        embedded.to_update_element()
        self.assertTrue(embedded.element_have_params(new_params_list))
        embedded.delete_element()
        self.assertFalse(embedded.have_element())