#coding=utf-8
from __future__ import unicode_literals
import random
from basetest import BaseTest
from pages.main_page import MainPage


class TestsAnalogs(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_analog()

    def test01_add_and_remove_analog(self):
        analog = self.item
        analog.add_item(analog.item_name)
        self.assertTrue(analog.have_item(analog.item_name))
        analog.delete_item(analog.item_name)
        self.assertFalse(analog.have_item(analog.item_name))

    def test02_add_and_remove_group(self):
        analog = self.item
        analog.choose_item(analog.item_number)
        num_of_elements = analog.get_number_of_elements()
        element_text = analog.add_group()
        self.assertTrue(analog.have_element(element_text, num_of_elements))
        analog.delete_element()
        analog.choose_item(analog.item_number)
        self.assertFalse(analog.have_element(element_text, num_of_elements))

    def test03_add_and_remove_element(self):
        analog = self.item
        analog.choose_item(analog.item_number)
        num_of_elements = analog.get_number_of_elements()
        element_text = analog.add_element({})
        self.assertTrue(analog.have_element(element_text, num_of_elements))
        analog.delete_element()
        analog.choose_item(analog.item_number)
        self.assertFalse(analog.have_element(element_text, num_of_elements))

    def test04_change_analog_name(self):
        analog = self.item
        new_analog_name = "test_QWERT_" + str(random.randrange(0, 150))
        old_analog_name = analog.get_item_name_by_num(analog.item_number)
        analog.change_item_name(old_analog_name, new_analog_name)
        self.assertTrue(analog.have_item(new_analog_name))
        analog.change_item_name(new_analog_name, old_analog_name)