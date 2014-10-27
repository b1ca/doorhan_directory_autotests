#coding=utf-8
from __future__ import unicode_literals
import random

from basetest import BaseTest
from pages.main_page import MainPage


class TestsShields2(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_shield()

    def test06_add_shield(self):
        shield = self.item
        params_list = [
            ["option", ["Создать щит на базе группы", "С защитой от защемления пальцев 500+610 RSD02"]],
            ["option", ["Тип панели", "С защитой от защемления"]],
            ["option", ["Дизайн панели", "Филенка с переменным шагом"]],
            ["option", ["Дизайн панели 2", "Волна, легкие"]],
            ["option", ["Структура панели", "Гладкая - Ндерево"]],
            ["option", ["Цвет панели внутри", "FOREST WALNUT"]],
            ["option", ["Цвет панели снаружи", "ZEBRA"]],
            ["checkbox_weight_code", ["500", "8", "00000000018"]],
            ["checkbox_weight_code", ["525", "10", "00000000019"]],
            ["checkbox_weight_code", ["575", "25", "00000000020"]],
            ["checkbox_weight_code", ["610", "3", "00000000021"]],
            ["checkbox_weight_code", ["530", "13", "00000000015"]],
            ["fx", ["Только один типоразмер разрешен:", "0"]],
            ["option", ["Шаг филенки", "350"]],
            ["option", ["Ширина квадрата филенки", "450"]],
            ["option", ["Высота квадрата филенки", "300"]],
            ["region", ["Европа"]],
        ]
        shield._add_shield(params_list)

    def test07_change_group(self):
        shield = self.item
        shield_name = "test_QWERT_" + str(random.randrange(0, 150))
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
        shield.add_group(shield_name, params_list)
        shield.to_update_group(shield_name)
        new_params_list = [
            ["fx", ["Число вариантов автонадставки", "3"]],
            ["fx", ["Варианты автонадставки", "0"]],
        ]
        shield.update_group(new_params_list)
        self.assertTrue(shield.have_item(shield_name))
        self.assertTrue(shield.group_have_params(shield_name, new_params_list))
        shield.delete_group(shield_name)
        self.assertFalse(shield.have_item(shield_name))

    def test08_change_shield(self):
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
            ["fx", ["Только один типоразмер разрешен:", "1"]],
        ]
        group_name = params_list[0][1][1]
        shield.add_shield(params_list)
        shield.choose_group(group_name)
        shield.choose_nth_item(0)
        new_params_list = [
            ["option", ["Цвет панели снаружи", "RAL9003"]],
            ["checkbox_weight_code", ["500", "10", "00000000005"]],
            ["checkbox_weight_code", ["550", "12", "00000000006"]],
        ]
        shield.update_shield(new_params_list)
        shield.choose_group(group_name)
        shield.choose_nth_item(0)
        self.assertTrue(shield.shield_has_params(new_params_list))
        shield.choose_group(group_name)
        shield.delete_added_element()