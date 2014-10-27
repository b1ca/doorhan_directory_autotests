#coding=utf-8
from __future__ import unicode_literals
import logging
import sys
import unittest

from testconfig import config
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER

from helpers.screenshooter import get_screenshot
from pages.login_page import LoginPage


URL = 'http://146.185.169.28/doorhan_test/'
LOGIN = config['login']
PASS = config['pass']
LOGGER.setLevel(logging.WARNING)


class BaseTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.implicitly_wait(20)
        login_page = LoginPage(self.driver)
        login_page.navigate()
        login_page.do_login(LOGIN, PASS)

    def tearDown(self):
        if sys.exc_info()[0]:
            get_screenshot(self)
        if not 'debug' in config:
            self.driver.get(''.join([LoginPage.url, 'site/logout']))
        # self.driver.get(''.join([LoginPage.url, 'site/logout']))

    @classmethod
    def tearDownClass(cls):
        if not 'debug' in config and cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()