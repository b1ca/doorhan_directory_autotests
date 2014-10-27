#coding=utf-8
from __future__ import unicode_literals


class BasePage(object):
    url = 'http://146.185.169.28/doorhan_test/'

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)