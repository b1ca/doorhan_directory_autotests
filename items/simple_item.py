# coding=utf-8
from __future__ import unicode_literals

import time

from helpers.waits import *
from helpers.actions_by_label_text import *
from helpers.nomenclature_dialog import choose_random_element_from_dict


class SimpleItem(object):
    """
    parent class for - embedded, driver, nomenclatureAdditional,
    nomenclatureAdditionalMaterial, driverSet, service, color
    """
    def __init__(self, driver):
        self.driver = driver

    item_type = None
    item = None
    element_text = None
    title_position = 4
    css_selector_for_add_element_btn = "a[href*='add']"
    product_mark = None

    def add_element(self, element_params):
        self.driver.find_element_by_css_selector(self.css_selector_for_add_element_btn).click()
        self.driver.find_element_by_css_selector("a[onclick*='#dictionary-nomenclature']").click()
        self.element_text = choose_random_element_from_dict(self)
        self._update_element_params(element_params)

    def _update_element_params(self, element_params):
        raise NotImplementedError

    def do_action(self, act):
        action = act[0]
        label_text = act[1][0]
        text_to_do = ""
        try:
            text_to_do = act[1][1]
        except LookupError:
            pass
        if action == "checkbox":
            self.click_checkbox_by_label_text(label_text)
        elif action == "option":
            get_option_by_label_text(self, label_text, text_to_do).click()
            wait_until_jquery(self, 5)
        elif action == "input":
            self.sendkeys_by_label_text(label_text, text_to_do)
        elif action == "fx":
            if len(act[1]) == 3:
                num = act[1][2]
            else:
                num = 0
            get_fx_element_by_label_text(self, label_text, num).click()
            self.driver.find_element_by_xpath("(//div[@class='module-tab'])[last()]").clear()
            self.driver.find_element_by_xpath("(//div[@class='module-tab'])[last()]").send_keys(text_to_do)
            self.driver.find_element_by_xpath("(//span[@class='ui-button-text'][text()='Ок'])[last()]").click()
            time.sleep(3)
        elif action == "checkbox_weight_code":
            element = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '%s']/..//input[not(@type = 'hidden')]" % label_text)
            element_id = element.get_attribute("value")
            element.click()
            self.driver.find_element_by_css_selector(
                "input[name='ShieldModel[panelWeight][%s]']" % element_id).send_keys(act[1][1])
            self.driver.find_element_by_css_selector(
                "input[data-id='%s'][type='text']" % element_id).send_keys(act[1][2])
            self.driver.find_elements_by_xpath("//ul[contains(@class, 'ui-autocomplete')]"
                                               "[contains(@style, 'display: block')]"
                                               "//a[contains(text(),'%s')]" % act[1][2])[0].click()
        elif action == "radio":
            element = self.driver.find_element_by_xpath(
                "//label[text()='%s']/..//label[text()='%s']" % (label_text, text_to_do))
            element_id = element.get_attribute("for")
            self.driver.find_element_by_id(element_id).click()
        elif action == "version":
            self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
            for version in act[1]:
                self.driver.find_element_by_xpath("//label[contains(text(), '%s')]" % version).click()
        elif action == "region":
            self.driver.find_element_by_xpath("//a[contains(text(), 'Регион')]").click()
            for region in act[1]:
                self.driver.find_element_by_xpath("//span[text()='%s']/../input" % region).click()

    def sendkeys_by_label_text(self, label_text, text_to_type):
        element = self.driver.find_element_by_xpath("//label[normalize-space(text()) = '%s']/../..//input" % label_text)
        element.clear()
        element.send_keys(text_to_type)

    def click_checkbox_by_label_text(self, label_text):
        element = get_element_by_label_text(self, label_text)
        if element.is_selected():
            print label_text+" is already selected"
        else:
            element.click()

    def get_checkbox_by_label_text(self, label_text):
        return get_element_by_label_text(self, label_text)

    def check_params_on_page(self, param):
        action = param[0]
        label_text = param[1][0]
        text_to_do = ""
        try:
            text_to_do = param[1][1]
        except LookupError:
            pass
        if action == "checkbox":
            return self.get_checkbox_by_label_text(label_text).is_selected()
        if action == "input":
            element = get_input_by_label_text(self, label_text)
            return element.get_attribute("value").strip() == text_to_do.strip()
        if action == "option":
            # res = self.get_option_by_label_text(label_text, text_to_do).is_selected()
            # print "option = %s" % res
            return get_option_by_label_text(self, label_text, text_to_do).is_selected()
        if action == "fx":
            if len(param[1]) == 3:
                num = param[1][2]
            else:
                num = 0
            # val = self.get_elements_by_label_text(label_text)[num].get_attribute("value").strip()
            # print "fx: val = %s, text_to_do = %s" % (val, text_to_do)
            return get_elements_by_label_text(self, label_text)[num].get_attribute("value").strip() == text_to_do
        if action == "checkbox_weight_code":
            chkbox = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '%s']/..//input[not(@type = 'hidden')]" % param[1][0])
            element_id = chkbox.get_attribute("value")
            weight_input_val = self.driver.find_element_by_css_selector(
                "input[name='ShieldModel[panelWeight][%s]']" % element_id).get_attribute("value")
            code_input_val = self.driver.find_element_by_css_selector(
                "input[data-id='%s'][type='text']" % element_id).get_attribute("value")
            result = chkbox.is_selected() and weight_input_val in param[1][1] and code_input_val in param[1][2]
            return result
        if action == "radio":
            element = self.driver.find_element_by_xpath(
                "//label[text()='%s']/..//label[text()='%s']" % (label_text, text_to_do))
            element_id = element.get_attribute("for")
            return self.driver.find_element_by_id(element_id).is_selected()
        if action == "version":
            self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
            result = True
            for version in param[1]:
                el_id = self.driver.find_element_by_xpath(
                    "//label[contains(text(), '%s')]" % version).get_attribute("for")
                result = result and self.driver.find_element_by_id(el_id).is_selected()
            return result
        if action == "region":
            self.driver.find_element_by_xpath("//a[contains(text(), 'Регион')]").click()
            result = True
            for region in param[1]:
                el = self.driver.find_element_by_xpath("//span[text()='%s']/../input" % region)
                result = result and el.is_selected()
            return result

    def have_element(self):
        element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(%s)" % str(self.title_position))[0]
        return self.element_text.strip() == element.text.strip()

    def element_have_params(self, element_params):
        result = self._element_have_params(element_params)
        self.driver.find_element_by_css_selector(".btn-white a").click()
        return result

    def _element_have_params(self, element_params):
        return all(self.check_params_on_page(param) for param in element_params)

    def save_element(self):
        raise NotImplementedError

    def to_update_element(self):
        wait_until_jquery(self, 10)
        self.driver.find_element_by_css_selector("a.update").click()

    def delete_element(self):
        self.driver.find_elements_by_css_selector("tbody input")[0].click()
        self.driver.find_element_by_css_selector("#listSubmit").click()

    def add_product(self, product_params=()):
        product_count = 0
        product_type = 'RSD 02'
        checkbox_maps = ('Цех',)
        if len(product_params) == 3:
            product_count, product_type, checkbox_maps = product_params
        product = self.driver.find_element_by_css_selector(".products[count='%s']" % str(product_count))
        product_field = product.find_element_by_css_selector(".autocompleteProducts")
        product_field.click()
        product_field.clear()
        product_field.send_keys(product_type)
        product.find_element_by_xpath("//a[.='%s']" % product_type).click()
        time.sleep(2)
        product.find_elements_by_css_selector(
            "select[name*='%sModel[%s]'] option[value]" % (self.product_mark, product_count))[0].click()
        product.find_element_by_css_selector('.ui-multiselect').click()
        time.sleep(1)
        for_attr = ('Model_0_card_id', 'Model_0_card_id') if not product_count else (
            'Model_card_id', 'Model_%s_card_id' % product_count)
        for checkbox_text in checkbox_maps:
            self.driver.find_element_by_xpath(
                "//*[contains(@for, '%s')][.='%s']/input | //*[contains(@for, '%s')][.='%s']/input"
                % (for_attr[0], checkbox_text, for_attr[1], checkbox_text)).click()

    def update_product(self, new_product_params):
        if not len(new_product_params) == 3:
            raise Exception('product params must be tuple or list of 3 elements.')
        self.add_product(new_product_params)

    def element_have_product(self, product_params):
        self.driver.implicitly_wait(2)
        product_count, product_type, checkbox_maps = product_params
        try:
            products = self.driver.find_elements_by_css_selector(".products[count='%s']" % str(product_count))
            product = products[0]
            product_result = len(products) == 1
            product_field_result = product.find_element_by_css_selector(
                ".autocompleteProducts").get_attribute("value") == product_type
            checkbox_maps_result = []
            product.find_element_by_css_selector('.ui-multiselect').click()
            for_attr = 'Model_%s_card_id' % product_count
            for checkbox_text in checkbox_maps:
                checkbox_maps_result.append(self.driver.find_element_by_xpath(
                    "//*[contains(@for, '%s')][.='%s']/input" % (for_attr, checkbox_text)).is_selected())
            checkbox_maps_result = all(checkbox_maps_result)
            return all([product_result, product_field_result, checkbox_maps_result])
        except IndexError, e:
            print e.message
            return False

    def delete_product(self, product_count):
        self.driver.find_element_by_css_selector(".products[count='%s'] [class*=deleteProduct]" % product_count).click()
        wait_until_jquery(self, 5)

    def add_second_product(self, product_params):
        self.driver.find_element_by_css_selector('.new-delete #addInputAutoComplete').click()
        self.add_product(product_params)

    def update_second_product(self, products_params):
        self.update_product(products_params)

    def delete_second_product(self, product_count=1):
        self.delete_product(product_count)
        self.save_element()