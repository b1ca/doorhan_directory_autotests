#coding=utf-8
from __future__ import unicode_literals
import pages
import basetest
import random


class TestDirAnalogs(basetest.BaseTest):

    def test01_add_and_remove_analog(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        analog = constructor_page.navigate_analog()
        analog_name = "test_QWERT_" + str(random.randrange(0, 150))
        analog.add_item(analog_name)
        self.assertTrue(analog.have_item(analog_name))
        analog.delete_item(analog_name)
        self.assertFalse(analog.have_item(analog_name))

    def test02_add_and_remove_group(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        analog = constructor_page.navigate_analog()
        num_of_analog = random.randrange(0, 10)
        analog.choose_item(num_of_analog)
        num_of_elements = analog.get_number_of_elements()
        element_text = analog.add_group()
        self.assertTrue(analog.have_element(element_text, num_of_elements))
        analog.delete_added_element()
        analog.choose_item(num_of_analog)
        self.assertFalse(analog.have_element(element_text, num_of_elements))

    def test03_add_and_remove_element(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        analog = constructor_page.navigate_analog()
        num_of_analog = random.randrange(0, 10)
        analog.choose_item(num_of_analog)
        num_of_elements = analog.get_number_of_elements()
        element_text = analog.add_element({})
        self.assertTrue(analog.have_element(element_text, num_of_elements))
        analog.delete_added_element()
        analog.choose_item(num_of_analog)
        self.assertFalse(analog.have_element(element_text, num_of_elements))

    def test04_change_analog_name(self):
        main_page = pages.MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        analog = constructor_page.navigate_analog()
        num_of_analog = random.randrange(0, 10)
        new_analog_name = "test_QWERT_" + str(random.randrange(0, 150))
        old_analog_name = analog.get_item_name_by_num(num_of_analog)
        analog.change_item_name(old_analog_name, new_analog_name)
        self.assertTrue(analog.have_item(new_analog_name))
        analog.change_item_name(new_analog_name, old_analog_name)