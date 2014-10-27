#coding=utf-8
from __future__ import unicode_literals
import random
from basetest import BaseTest
from pages.main_page import MainPage


class TestsGroups(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_group()

    def test01_add_and_remove_group(self):
        group = self.item
        group_name = "test_QWERT_" + str(random.randrange(0, 150))
        group.add_item(group_name)
        self.assertTrue(group.have_item(group_name))
        group.delete_item(group_name)
        self.assertFalse(group.have_item(group_name))

    def test02_add_and_remove_element(self):
        group = self.item
        group.add_group_with_params({"color": "КОРИЧН. МУАР", "Версия": ["Внутренняя"], "Регион": []})

    def test03_add_and_remove_element(self):
        group = self.item
        group.add_group_with_params({"color": "Коричневый", "Версия": [], "Регион": ["Европа"]})

    def test04_change_group_name(self):
        group = self.item
        num_of_group = random.randrange(0, 10)
        new_group_name = "test_QWERT_" + str(random.randrange(0, 150))
        old_group_name = group.get_item_name_by_num(num_of_group)
        group.change_item_name(old_group_name, new_group_name)
        self.assertTrue(group.have_item(new_group_name))
        group.change_item_name(new_group_name, old_group_name)
        self.assertTrue(group.have_item(old_group_name))

    def test05_change_element_param(self):
        group = self.item
        num_of_group = random.randrange(0, 10)
        group.choose_item(num_of_group)
        num_of_elements = group.get_number_of_elements()
        element_to_change = 0
        if num_of_elements > 1:
            element_to_change = random.randrange(0, num_of_elements - 1)
        params_dict = {"color": "Коричневый", "Версия": [], "Регион": []}
        old_color = group.change_element_params(element_to_change, params_dict)
        print "old_color = %s" % old_color
        self.assertTrue(group.element_has_params(0, params_dict))
        params_dict["color"] = old_color
        group._update_element_params(params_dict)