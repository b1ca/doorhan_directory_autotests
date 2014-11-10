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
        pass

    def test10_update_group_of_covers(self):
        pass

    def test11_add_cover(self):
        pass

    def test12_add_cover_as_group(self):
        pass

    def test13_update_cover(self):
        pass

    def test14_remove_cover(self):
        pass

    def test15_remove_group_of_covers(self):
        pass