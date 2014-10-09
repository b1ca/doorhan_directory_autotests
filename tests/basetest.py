#coding=utf-8
from __future__ import unicode_literals
import logging
import os
import sys
import unittest

from testconfig import config
import pages

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
from datetime import datetime

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
        login_page = pages.LoginPage(self.driver)
        login_page.navigate()
        login_page.do_login(LOGIN, PASS)

    def tearDown(self):
        if sys.exc_info()[0]:
            method_name = self._testMethodName
            class_name = type(self).__name__
            time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            folder = os.path.dirname(os.getcwd())
            directory = "".join([folder, "/test-results/", class_name])

            if not os.path.exists(directory):
                os.makedirs(directory)

            file_name = "%s/%s - %s.png" % (directory, time_now, method_name)

            self.driver.get_screenshot_as_file(file_name)
            # for jenkins integration
            print "[[ATTACHMENT|%s]]" % file_name
            print "current url - %s" % self.driver.current_url
        if not 'debug' in config:
            self.driver.get(''.join([pages.LoginPage.url, 'site/logout']))

    @classmethod
    def tearDownClass(cls):
        if not 'debug' in config and cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()