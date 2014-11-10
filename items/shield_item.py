# coding=utf-8
from __future__ import unicode_literals
import random
import time

from base_item import BaseItem
from helpers.actions_by_label_text import get_elements_by_label_text
from helpers.nomenclature_dialog import choose_random_element_from_dict
from simple_item import SimpleItem
from helpers.waits import *


class Shield(BaseItem, SimpleItem):

    item_type = "shield"
    item_name = "test_QWERT_" + str(random.randrange(0, 150))
    cover_name = "test_cover_" + str(random.randrange(0, 150))
    group_name = 'RH58'
    element_text = None

    def add_group(self, shield_name, params_list, add_new_product=0):
        self.driver.find_element_by_css_selector("a[href$='addGroup']").click()
        self.driver.find_element_by_css_selector("#ShieldGroupModel_title").clear()
        self.driver.find_element_by_css_selector("#ShieldGroupModel_title").send_keys(shield_name)

        self.driver.find_element_by_xpath(
            '//span[contains(text(), "Наименование")]/..//button[contains(@class, "ui-multiselect")]').click()
        self.driver.find_element_by_xpath('//span[.="RSD 02"]').click()
        time.sleep(5)

        checkbox_text = 'Цех'
        self.driver.find_element_by_xpath(
            '//span[contains(text(), "Карты")]/..//button[contains(@class, "ui-multiselect")]').click()
        self.driver.find_element_by_xpath('//span[.="%s"]' % checkbox_text).click()
        wait_until_jquery(self, 10)
        self.update_group(params_list)

    def update_group(self, params_list):
        for param in params_list:
            self.do_action(param)
        self.driver.find_element_by_css_selector("#yt2").click()

    def to_update_group(self, group_name):
            self.driver.find_element_by_xpath("//a[text()='"+group_name+"']/../a[contains(@class, 'edit')]").click()

    def group_have_params(self, shield_name, params_list):
        self.driver.find_element_by_xpath("//a[text()='"+shield_name+"']/..//a[@class='shield-group-action edit']")\
            .click()
        result = all(self.check_params_on_page(param) for param in params_list)
        self.driver.find_element_by_css_selector(".btn-white a").click()
        return result

    def have_item(self, item_name):
        el = self.driver.find_elements_by_xpath("//a[text()='"+item_name+"']")
        return len(el) == 1

    def delete_group(self, group_name):
        delete_btn = self.driver.find_element_by_xpath(
            "//a[text()='"+group_name+"']/..//a[@class='shield-group-action delete']")
        delete_btn.click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        wait_until_jquery(self, 10)
        self.driver.implicitly_wait(2)

    def add_shield(self, params_list):
        self.driver.find_element_by_css_selector("#add_shield").click()
        self.update_shield(params_list)

    def update_shield(self, params_list):
        for param in params_list:
            self.do_action(param)

        self.driver.find_element_by_css_selector("#yt0").click()

    def choose_group(self, group_name):
        self.driver.find_element_by_xpath(
            "//a[contains(@class,'shield-group')][starts-with(.,'%s')]" % group_name).click()

    def shield_has_params(self, params_list):
        result = all(self.check_params_on_page(param) for param in params_list)
        self.driver.find_element_by_css_selector(".btn-white a").click()
        return result

    def delete_added_element(self):
        delete_btn = self.driver.find_element_by_css_selector(".tbl a.delete")
        delete_btn.click()

        alert = self.driver.switch_to_alert()
        alert.accept()
        wait_until_jquery(self, 5)
        import time
        time.sleep(3)

    def click_checkbox_by_label_text(self, label_text):
        element = get_elements_by_label_text(self, label_text)[0]
        if element.is_selected():
            print label_text+" is already selected"
        else:
            element.click()

    def get_checkbox_by_label_text(self, label_text):
        return get_elements_by_label_text(self, label_text)[0]

    def choose_nth_item(self, n):
        self.driver.find_elements_by_css_selector("a.update")[n].click()

    def _add_shield(self, params_list):
        group_name = params_list[0][1][1]
        self.add_shield(params_list)
        self.choose_group(group_name)
        self.choose_nth_item(0)
        assert self.shield_has_params(params_list)
        self.choose_group(group_name)
        self.delete_added_element()

    def choose_item_by_name(self, shield_name):
        self.driver.find_element_by_xpath("//a[contains(@class, 'shield-group')][.='%s']" % shield_name).click()
        wait_until_jquery(self, 10)

    def choose_cover_group_by_name(self, cover_name):
        self.driver.find_element_by_xpath("//a[contains(@class, 'cover-group')][.='%s']" % cover_name).click()
        wait_until_jquery(self, 10)

    def add_cover_group(self, cover_params):
        self.driver.find_element_by_css_selector("#add_cover_group").click()

        self.update_cover_group_name(self.cover_name)
        self.update_cover_group(cover_params)
        self.save_cover_group()

    def save_cover_group(self):
        self.driver.find_element_by_css_selector("#yt0").click()
        wait_until_jquery(self, 10)

    def to_update_cover_group(self):
        self.driver.find_element_by_xpath(
            "//a[@class='cover-group'][.='%s']/../../a[@class ='shield-group-action edit']" % self.cover_name).click()

    def update_cover_group(self, cover_params):
        for param in cover_params:
            self.do_action(param)

    def update_cover_group_name(self, cover_name):
        cover_input = self.driver.find_element_by_css_selector("#ShieldCoverGroupModel_title")
        cover_input.clear()
        cover_input.send_keys(cover_name)

    def have_cover_group(self, cover_name):
        self.driver.implicitly_wait(2)
        return len(self.driver.find_elements_by_xpath("//a[@class='cover-group'][.='%s']" % cover_name)) == 1

    def remove_cover_group(self, cover_name):
        self.driver.find_element_by_xpath(
            "//a[@class='cover-group'][.='%s']/../../a[@class ='shield-group-action delete']" % cover_name).click()
        self.driver.switch_to.alert.accept()
        wait_until_jquery(self, 10)

    def add_cover(self, cover_params, as_group=False):
        self.to_add_cover_page()
        self.update_cover(cover_params, as_group)
        self.add_product()
        self.save_cover()

    def to_add_cover_page(self):
        self.driver.find_element_by_css_selector("#add_cover").click()

    def update_cover(self, cover_params, as_group):
        if as_group:
            self.driver.find_element_by_css_selector("input[value='group']").click()
            group_input = self.driver.find_element_by_css_selector("#autocompleteGroups")
            group_input.click()
            group_input.clear()
            group_input.send_keys(self.group_name)
            self.driver.find_element_by_xpath("//a[.='%s']" % self.group_name).click()
            self.element_text = self.group_name
        else:
            self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
            self.element_text = choose_random_element_from_dict(self)
        for param in cover_params:
            self.do_action(param)

    def remove_cover(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector(".tbl a.delete").click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        wait_until_jquery(self, 10)

    def to_update_cover(self):
        self.driver.find_element_by_css_selector(".tbl a.update").click()

    def save_cover(self):
        self.driver.find_element_by_css_selector("#yt0").click()

    def add_product(self, product_params=()):
        product_type = 'RSD 02'
        checkbox_maps = ('Цех',)
        if len(product_params) == 3:
            _, product_type, checkbox_maps = product_params
        self.driver.find_element_by_xpath("//input[@id='ShieldCoverProductModel_product_id']/..//button").click()
        self.driver.find_element_by_xpath("//label[.='%s']/input" % product_type).click()
        time.sleep(2)
        self.driver.find_elements_by_css_selector(
            '#ShieldCoverProductModel_specification_id option:not([selected])')[0].click()
        self.driver.find_elements_by_css_selector('.ui-multiselect')[-1].click()
        time.sleep(1)
        for checkbox_text in checkbox_maps:
            self.driver.find_element_by_xpath("//label[.='%s']/input" % checkbox_text).click()

    def update_product(self, new_product_params):
        if not len(new_product_params) == 3:
            raise Exception('product params must be tuple or list of 3 elements.')
        self.add_product(new_product_params)

    def have_cover(self):
        el = self.driver.find_elements_by_xpath("//td[.='%s']" % self.element_text)
        return len(el) == 1