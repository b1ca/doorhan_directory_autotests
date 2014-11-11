#coding=utf-8
from __future__ import unicode_literals

from basetest import BaseTest
from pages.main_page import MainPage


class TestsShields3(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        main_page = MainPage(self.driver)
        constructor_page = main_page.navigate_cp()
        self.item = constructor_page.navigate_shield()

    def test09_add_group_of_covers(self):
        shield_name = "My_Custom_Shield"
        shield = self.item
        shield.choose_item_by_name(shield_name)
        cover_params = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        shield.add_cover_group(cover_params)
        self.assertTrue(shield.have_cover_group(shield.cover_name))
        shield.remove_cover_group(shield.cover_name)
        self.assertFalse(shield.have_cover_group(shield.cover_name))

    def test10_update_group_of_covers(self):
        shield_name = "My_Custom_Shield"
        shield = self.item
        shield.choose_item_by_name(shield_name)
        cover_params = [
            ["version", ["Внутренняя"]],
            ["region", ["СНГ"]],
        ]
        shield.add_cover_group(cover_params)
        self.assertTrue(shield.have_cover_group(shield.cover_name))
        new_cover_name = 'rrr'
        shield.to_update_cover_group()
        shield.update_cover_group_name(new_cover_name)
        shield.save_cover_group()
        self.assertTrue(shield.have_cover_group(new_cover_name))
        shield.remove_cover_group(new_cover_name)
        self.assertFalse(shield.have_cover_group(new_cover_name))

    def test11_add_cover(self):
        cover_name = "My_Custom_Cover"
        shield = self.item
        shield.choose_cover_group_by_name(cover_name)
        cover_params = [
            ["fx", ["Количество", "15"]],
        ]
        shield.add_cover(cover_params)
        self.assertTrue(shield.have_cover())
        shield.remove_cover()
        self.assertFalse(shield.have_cover())

    def test12_add_cover_as_group(self):
        cover_name = "My_Custom_Cover"
        shield = self.item
        shield.choose_cover_group_by_name(cover_name)
        cover_params = [
            ["fx", ["Количество", "15"]],
        ]
        shield.add_cover(cover_params, as_group=True)
        self.assertTrue(shield.have_cover())
        shield.remove_cover()
        self.assertFalse(shield.have_cover())

    def test13_update_cover(self):
        cover_name = "My_Custom_Cover"
        shield = self.item
        shield.choose_cover_group_by_name(cover_name)
        cover_params = [
            ["fx", ["Количество", "15"]],
        ]
        product_params = (0, 'ISD 01', ())
        shield.add_cover(cover_params)
        shield.to_update_cover()
        shield.add_product(product_params)
        shield.save_cover()
        self.assertTrue(shield.have_cover())
        shield.remove_cover()
        self.assertFalse(shield.have_cover())