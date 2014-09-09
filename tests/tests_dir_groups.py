#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest
import random


class TestDirGroups(basetest.BaseTest):

    def test01_add_and_remove_group(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        group = constructor_page.navigate_group()
        group_name = "test_QWERT_" + str(random.randrange(0, 150))
        group.add_item(group_name)
        self.assertTrue(group.have_item(group_name))
        group.delete_item(group_name)
        self.assertFalse(group.have_item(group_name))

    def add_element_with_params(self, params_dict):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        group = constructor_page.navigate_group()
        num_of_group = random.randrange(0, 10)
        group.choose_item(num_of_group)
        num_of_elements = group.get_number_of_elements()
        element_text = group.add_element(params_dict)
        self.assertTrue(group.have_element(element_text, num_of_elements))
        group.delete_added_element()
        group.choose_item(num_of_group)
        self.assertFalse(group.have_element(element_text, num_of_elements))

    def test02_add_and_remove_element(self):
        self.add_element_with_params({"color": "КОРИЧН. МУАР", "Версия": ["Внутренняя"], "Регион": []})

    def test03_add_and_remove_element(self):
        self.add_element_with_params({"color": "Коричневый", "Версия": [], "Регион": ["Европа"]})

    def test04_change_group_name(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        group = constructor_page.navigate_group()
        num_of_group = random.randrange(0, 10)
        new_group_name = "test_QWERT_" + str(random.randrange(0, 150))
        old_group_name = group.get_item_name_by_num(num_of_group)
        print "old_group_name = %s" % old_group_name
        group.change_item_name(old_group_name, new_group_name)
        self.assertTrue(group.have_item(new_group_name))
        group.change_item_name(new_group_name, old_group_name)

    def test05_change_element_param(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        group = constructor_page.navigate_group()
        num_of_group = random.randrange(0, 10)
        group.choose_item(num_of_group)
        num_of_elements = group.get_number_of_elements()
        element_to_change = 0
        if num_of_elements > 1:
            element_to_change = random.randrange(0, num_of_elements - 1)
        params_dict = {"color": "Белый", "Версия": [], "Регион": []}
        old_color = group.change_element_params(element_to_change, params_dict)
        print "old_color = %s" % old_color
        self.assertTrue(group.element_has_params(0, params_dict))
        params_dict["color"] = old_color + " "
        group.update_element_params(params_dict)