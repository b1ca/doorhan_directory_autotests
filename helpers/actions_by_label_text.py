# coding=utf-8
from __future__ import unicode_literals


def get_option_by_label_text(self, label_text, option):
    return self.driver.find_element_by_xpath(
        "//label[starts-with(.,'%s')]/..//select/option[starts-with(.,'%s')]" % (label_text, option))


def get_input_by_label_text(self, label_text):
    return get_element_by_label_text(self, label_text)


def get_fx_element_by_label_text(self, label_text, n):
    element = self.driver.find_elements_by_xpath(
        "//label[starts-with(.,'%s')]/..//a | //span[starts-with(.,'%s')]/..//a" % (label_text, label_text))[n]
    return element


def get_element_by_label_text(self, label_text):
    element = self.driver.find_element_by_xpath("//label[normalize-space(text()) = '%s']" % label_text)
    element_id = element.get_attribute("for")
    return self.driver.find_element_by_id(element_id)


def get_elements_by_label_text(self, label_text):
    elements = self.driver.find_elements_by_xpath(
        "//label[starts-with(.,'%s')]/..//input[not(@type = 'hidden')]" % label_text)
    return elements