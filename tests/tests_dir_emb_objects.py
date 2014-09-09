#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest
import random


class TestDirEmbObjects(basetest.BaseTest):

    def add_embedded_element(self, embedded_type, params_list):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        embedded = constructor_page.navigate_embedded()
        embedded_name = params_list[0][1][1]
        if embedded_type == "kalitka":
            embedded.choose_kalitka_type()
        elif embedded_type == "window":
            embedded.choose_window_type()
        element_number = embedded.get_number_of_elements()
        element_text = embedded.add_embedded_element(embedded_name, params_list)
        print element_text
        self.assertTrue(embedded.have_element(element_text, element_number))
        embedded.choose_nth_item(0)
        self.assertTrue(embedded.embedded_has_params(params_list))
        embedded.delete_added_element()
        self.assertFalse(embedded.have_element(element_text, element_number))

    def test01_add_kalitka_element(self):
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        self.add_embedded_element("kalitka", params_list)

    def test02_add_kalitka_element(self):
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        self.add_embedded_element("kalitka", params_list)

    def test03_add_kalitka_element(self):
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        self.add_embedded_element("kalitka", params_list)

    def test04_add_window_element(self):
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        self.add_embedded_element("window", params_list)

    def test05_add_window_element(self):
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        self.add_embedded_element("window", params_list)

    def test06_change_kalitka_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        embedded = constructor_page.navigate_embedded()
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        embedded.choose_kalitka_type()
        element_number = embedded.get_number_of_elements()
        element_text = embedded.add_embedded_element(embedded_name, params_list)
        self.assertTrue(embedded.have_element(element_text, element_number))
        embedded.choose_nth_item(0)
        new_params_list = [
            ["fx", ["Слева", "10"]],
            ["fx", ["Сверху", "15"]],
            ["fx", ["Справа", "20"]],
            ["fx", ["Снизу", "25"]],
        ]
        embedded.update_element_params(new_params_list)
        embedded.choose_nth_item(0)
        self.assertTrue(embedded.embedded_has_params(new_params_list))
        embedded.delete_added_element()
        self.assertFalse(embedded.have_element(element_text, element_number))

    def test07_change_window_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        embedded = constructor_page.navigate_embedded()
        embedded_name = "test_QWERT_" + str(random.randrange(0, 150))
        params_list = [
            ["input", ["Название", embedded_name]],
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
        embedded.choose_window_type()
        element_number = embedded.get_number_of_elements()
        element_text = embedded.add_embedded_element(embedded_name, params_list)
        self.assertTrue(embedded.have_element(element_text, element_number))
        embedded.choose_nth_item(0)
        new_params_list = [
            ["input", ["Название", "TEMP_NAME"]],
            ["input", ["Радиус", "30"]],
            ["input", ["Артикул", "30"]],
            ["input", ["Вес", "30"]],
        ]
        embedded.update_element_params(new_params_list)
        embedded.choose_nth_item(0)
        self.assertTrue(embedded.embedded_has_params(new_params_list))
        embedded.delete_added_element()
        self.assertFalse(embedded.have_element(element_text, element_number))