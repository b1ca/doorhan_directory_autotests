#coding=utf-8
from __future__ import unicode_literals

from basetest import BaseTest
from pages.main_page import MainPage


class TestsShields(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_shield()

    def test01_add_group_shield(self):
        shield = self.item
        params_list = [
            ["checkbox", ["Возможно установить калитку"]],
            ["checkbox", ["Возможно установить окна"]],
            ["option", ["Ориентация панели", "Горизонтальная"]],
            ["fx", ["Верхний допуск на размер щита", "12"]],
            ["fx", ["Нижний допуск на размер щита", "3"]],
            ["fx", ["Отступ между панелями", "1"]],
            ["fx", ["Минимальный размер верхней панели", "5"]],
            ["fx", ["Минимальный размер нижней панели", "5"]],
            ["fx", ["Максимальный размер верхней панели", "20"]],
            ["fx", ["Максимальный размер нижней панели", "20"]],
            ["fx", ["Минимальный отрез верхней панели", "3"]],
            ["fx", ["Минимальный отрез нижней панели", "3"]],
            ["fx", ["Уменьшение при срезе верхней", "5"]],
            ["fx", ["Уменьшение при срезе нижней", "0"]],
            ["fx", ["Упаковочное место", "0"]],
            ["fx", ["Не резать по усилению", "1"]],
            ["fx", ["Только один типоразмер разрешен", "1"]],
            ["fx", ["Автонадставка профилем разрешена", "1", 0]],
            ["fx", ["Автонадставка профилем разрешена", "1", 1]],
            ["fx", ["Автонадставка по умолчанию", "0"]],
            ["fx", ["Число вариантов автонадставки", "2"]],
            ["fx", ["Варианты автонадставки", "1"]],
        ]
        shield.add_group(shield.item_name, params_list, add_new_product=0)
        self.assertTrue(shield.have_item(shield.item_name))
        self.assertTrue(shield.group_have_params(shield.item_name, params_list))
        shield.delete_group(shield.item_name)
        self.assertFalse(shield.have_item(shield.item_name))

    def test02_add_group_shield(self):
        shield = self.item
        params_list = [
            ["option", ["Ориентация панели", "Вертикальная"]],
            ["fx", ["Верхний допуск на размер щита", "30"]],
            ["fx", ["Нижний допуск на размер щита", "2"]],
            ["fx", ["Отступ между панелями", "2"]],
            ["fx", ["Минимальный размер верхней панели", "2"]],
            ["fx", ["Минимальный размер нижней панели", "2"]],
            ["fx", ["Максимальный размер верхней панели", "30"]],
            ["fx", ["Максимальный размер нижней панели", "30"]],
            ["fx", ["Минимальный отрез верхней панели", "0"]],
            ["fx", ["Минимальный отрез нижней панели", "0"]],
            ["fx", ["Уменьшение при срезе верхней", "3"]],
            ["fx", ["Уменьшение при срезе нижней", "0"]],
            ["fx", ["Упаковочное место", "0"]],
            ["fx", ["Не резать по усилению", "0"]],
            ["fx", ["Только один типоразмер разрешен", "0"]],
            ["fx", ["Автонадставка профилем разрешена", "0", 0]],
            ["fx", ["Автонадставка профилем разрешена", "1", 1]],
            ["fx", ["Автонадставка по умолчанию", "0"]],
            ["fx", ["Число вариантов автонадставки", "2"]],
            ["fx", ["Варианты автонадставки", "1"]],
        ]
        shield.add_group(shield.item_name, params_list, add_new_product=0)
        self.assertTrue(shield.have_item(shield.item_name))
        self.assertTrue(shield.group_have_params(shield.item_name, params_list))
        shield.delete_group(shield.item_name)
        self.assertFalse(shield.have_item(shield.item_name))

    def test03_add_shield(self):
        shield = self.item
        params_list = [
            ["option", ["Создать щит на базе группы", "Без защиты от защемления пальцев 475+500+525+550+575 RSD02"]],
            ["option", ["Тип панели", "Без защиты от защемления"]],
            ["option", ["Дизайн панели", "С центральной полосой"]],
            ["option", ["Дизайн панели 2", "Без волны"]],
            ["option", ["Структура панели", "Гладкая - Гладкая"]],
            ["option", ["Цвет панели внутри", "ALDER"]],
            ["option", ["Цвет панели снаружи", "RAL1014"]],
            ["checkbox_weight_code", ["385", "10", "00000000005"]],
            ["checkbox_weight_code", ["475", "12", "00000000006"]],
            ["checkbox_weight_code", ["500", "14", "00000000011"]],
            ["fx", ["Только один типоразмер разрешен:", "1"]],
            ["version", ["Внутренняя"]],
        ]
        shield._add_shield(params_list)

    def test04_add_shield(self):
        shield = self.item
        params_list = [
            ["option", ["Создать щит на базе группы", "Панели с алюминиевой облицовкой RSD02"]],
            ["option", ["Тип панели", "С защитой от защемления"]],
            ["option", ["Дизайн панели", "Без горизонтальной полосы"]],
            ["option", ["Дизайн панели 2", "Волна"]],
            ["option", ["Структура панели", "Нстукко - Нстукко"]],
            ["option", ["Цвет панели внутри", "GOLDEN OAK"]],
            ["option", ["Цвет панели снаружи", "RAL7004"]],
            ["checkbox_weight_code", ["475", "10", "00000000014"]],
            ["checkbox_weight_code", ["525", "12", "00000000013"]],
            ["checkbox_weight_code", ["550", "13", "00000000015"]],
            ["fx", ["Только один типоразмер разрешен:", "1"]],
            ["version", ["Дилерская"]],
        ]
        shield._add_shield(params_list)

    def test05_add_shield(self):
        shield = self.item
        params_list = [
            ["option", ["Создать щит на базе группы", "Панели с алюминиевой облицовкой 2010 RSD02"]],
            ["option", ["Тип панели", "С защитой от защемления"]],
            ["option", ["Дизайн панели", "Филенка"]],
            ["option", ["Дизайн панели 2", "Без волны"]],
            ["option", ["Структура панели", "Нстукко - Нстукко"]],
            ["option", ["Цвет панели внутри", "ALDER"]],
            ["option", ["Цвет панели снаружи", "ALDER"]],
            ["checkbox_weight_code", ["575", "5", "00000000014"]],
            ["checkbox_weight_code", ["610", "8", "00000000015"]],
            ["checkbox_weight_code", ["530", "10", "00000000011"]],
            ["checkbox_weight_code", ["562", "15", "00000000005"]],
            ["fx", ["Только один типоразмер разрешен:", "1"]],
            ["option", ["Шаг филенки", "260"]],
            ["option", ["Ширина квадрата филенки", "505"]],
            ["option", ["Высота квадрата филенки", "340"]],
            ["region", ["СНГ"]],
        ]
        shield._add_shield(params_list)