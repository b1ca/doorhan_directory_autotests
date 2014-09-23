#coding=utf-8
from __future__ import unicode_literals
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def wait_until_jquery(self, seconds_to_wait):
        jquery_active = lambda x: self.driver.execute_script("return jQuery.active == 0")
        WebDriverWait(self.driver, seconds_to_wait).until(jquery_active)

    def wait_until_jquery_is_ready(self, seconds_to_wait):
        jquery_is_ready = lambda x: self.driver.execute_script("return jQuery.isReady == true")
        WebDriverWait(self.driver, seconds_to_wait).until(jquery_is_ready)

    def wait_until_ui_dialog(self, seconds_to_wait):
        WebDriverWait(self.driver, seconds_to_wait).\
            until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog")))

    def wait_until_title_is_equal(self, seconds_to_wait, title):
        WebDriverWait(self.driver, seconds_to_wait).\
            until(EC.title_is(title))

    def wait_until_text_present(self, seconds_to_wait, locator, text):
        WebDriverWait(self.driver, seconds_to_wait).until(EC.text_to_be_present_in_element(locator, text))


class LoginPage(BasePage):
    url = "http://146.185.169.28/doorhan_test/"

    def do_login(self, login, password):
        self.driver.find_element_by_css_selector("#LoginForm_username").send_keys(login)
        self.driver.find_element_by_css_selector("#LoginForm_password").send_keys(password)
        self.driver.find_element_by_css_selector("input[type=submit]").click()
        return MainPage(self.driver)


class MainPage(BasePage):

    def navigate_cp(self):
        self.driver.find_element_by_css_selector("a[href$='constructor']").click()
        return ConstructorElement(self.driver)


class ConstructorElement(BasePage):

        item_type = None

        def navigate_group(self):
            self.navigate_item("group")
            return Group(self.driver)

        def navigate_analog(self):
            self.navigate_item("analog")
            return Analog(self.driver)

        def navigate_shield(self):
            self.navigate_item("shield")
            return Shield(self.driver)

        def navigate_embedded(self):
            self.navigate_item("embedded")
            return Embedded(self.driver)

        def navigate_driver(self):
            self.navigate_item("driver")
            return Driver(self.driver)

        def navigate_nomenclature_additional(self):
            self.navigate_item("nomenclatureAdditional")
            return NomenclatureAdditional(self.driver)

        def navigate_additional_material(self):
            self.navigate_item("nomenclatureAdditionalMaterial")
            return AdditionalMaterial(self.driver)

        def navigate_driver_set(self):
            self.navigate_item("driverSet")
            return DriverSet(self.driver)

        def navigate_service(self):
            self.navigate_item("service")
            return Service(self.driver)

        def navigate_color(self):
            self.navigate_item("colors")
            return Color(self.driver)

        def navigate_item(self, item_type, vertical_menu_css=".vertical-menu"):
            vertical_menu = self.driver.find_element_by_css_selector(vertical_menu_css)
            ActionChains(self.driver).move_to_element(vertical_menu).perform()
            self.driver.find_element_by_css_selector(vertical_menu_css + " a[href$="+item_type+"]").click()

        def add_item(self, item_name):
            self.driver.execute_script("$('#add-"+self.item_type+"').dialog('open');")  # open dialog add group
            add_item_form_input = self.driver.find_element_by_css_selector("#add-"+self.item_type+" input")
            add_item_form_input.send_keys(item_name)
            add_item_save_button = self.driver.find_element_by_css_selector("#add-"+self.item_type+" a.submit")
            add_item_save_button.click()

        def have_item(self, item_name):
            el = self.driver.find_elements_by_xpath("//span[text()='"+item_name+"']")
            return len(el) == 1

        def delete_item(self, item_name):
            delete_btn = self.\
                driver.find_element_by_xpath("//span[text()='"+item_name+"']/../..//div[@class='group-del']/a")
            delete_btn.click()
            import time
            time.sleep(3)
            self.driver.implicitly_wait(5)

        def get_item_name_by_num(self, num_of_item):
            return self.driver.find_elements_by_css_selector("span[class^="+self.item_type+"-title]")[num_of_item].text

        def change_item_name(self, old_item_name, new_item_name):
            self.driver.find_element_by_xpath("(//span[text()='"+old_item_name+"']/../..//a)[1]").click()
            item_name_input = self.driver.find_element_by_css_selector("#%s-title" % self.item_type)
            item_name_input.clear()
            item_name_input.send_keys(new_item_name)
            self.driver.find_element_by_css_selector("#edit-"+self.item_type+"-form a.submit").click()
            self.wait_until_jquery(10)

        def choose_item(self, num_of_item):
            self.driver.find_elements_by_css_selector("div[id^="+self.item_type+"-id]")[num_of_item].click()
            self.wait_until_jquery(5)

        def get_number_of_elements(self):
            return len(self.driver.find_elements_by_css_selector(".grid-view tr")) - 1

        def update_element_params(self, element_params):
            if element_params:
                if element_params["color"]:
                    color_field = self.driver.find_element_by_css_selector("#NomenclatureGroupElementsModel_color_val")
                    color_field.clear()
                    color_field.send_keys(element_params["color"])
                    self.wait_until_jquery(5)
                    if len(self.driver.find_elements_by_css_selector(".ui-menu-item a")) > 0:
                        self.driver.find_element_by_css_selector(".ui-menu-item a").click()
                if element_params["Версия"]:
                    self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
                    for v in element_params["Версия"]:
                        self.driver.find_element_by_xpath("//label[contains(text(), '"+v+"')]").click()
                if element_params["Регион"]:
                    #print "text = %s" % self.driver.find_elements_by_xpath("//a[contains(text(), 'Регион')]")[0].text
                    self.driver.find_elements_by_xpath("//a[contains(text(), 'Регион')]")[0].click()
                    for v in element_params["Регион"]:
                        self.driver.find_element_by_xpath("//*[@class='daredevel-tree-label'][text()='" + v +
                                                          "']/../input").\
                            click()
            self.driver.execute_script("$('#add-additional-element-form').submit();")

        def add_element(self, element_params, element_name="", selector="a[href*='add']"):
            self.driver.find_element_by_css_selector(selector).click()
            self.driver.execute_script("$('#dictionary-nomenclature').dialog('open'); return false;")
            element_text = self.choose_random_element_from_dict()
            self.update_element_params(element_params)
            return element_text

        def change_element_params(self, element_to_change, element_params):
            self.driver.find_elements_by_css_selector("a.update")[element_to_change].click()
            old_color = self.get_element_color()
            self.update_element_params(element_params)
            return old_color

        def get_element_color(self):
            return self.driver.find_element_by_css_selector("#NomenclatureGroupElementsModel_color_val").text

        def choose_random_element_from_dict(self):
            el_from_dict_list = self.driver.find_elements_by_xpath(
                "//ul[@class='treeview']//a[not(contains(., '___')) and not(contains(., 'goods for China'))]"
            )
            # number_to_click = random.randrange(0, len(el_from_dict_list))
            number_to_click = 0
            el_from_dict_list[number_to_click].click()
            self.wait_until_jquery(15)

            nomenclature_list = self.driver.find_elements_by_css_selector(".popup-nomenclature-table-container a")
            txt_lst = self.driver.find_elements_by_css_selector(".popup-nomenclature-table-container td:nth-of-type(3)")
            rand_num = random.randrange(0, len(nomenclature_list))
            rand_element = nomenclature_list[rand_num]
            element_text = txt_lst[rand_num].text
            rand_element.click()
            self.wait_until_jquery(5)
            return element_text

        def element_has_params(self, element_number, element_params):
            import time
            time.sleep(3)
            self.driver.find_elements_by_css_selector("a.update")[element_number].click()
            if element_params["color"]:
                color_field = self.driver.find_element_by_css_selector("#NomenclatureGroupElementsModel_color_val")
                return element_params["color"].lower() in color_field.get_attribute("value").lower()

        def have_element(self, element_text, num_of_elements):
            import time
            time.sleep(5)
            el_list = self.driver.find_elements_by_css_selector(".grid-view tr td:nth-of-type(3)")
            el_0_text = el_list[0].text
            # print "el_0_text = %s" % el_0_text
            # print "element_text = %s" % element_text
            # print "len(el_list) = %s" % len(el_list)
            # print "num_of_elements = %s" % num_of_elements
            return el_0_text == element_text and len(el_list) == num_of_elements + 1

        def delete_added_element(self):
            self.wait_until_jquery(5)
            self.driver.find_elements_by_css_selector("a.delete")[0].click()
            # self.driver.refresh()
            # import time
            # time.sleep(3)

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
                self.get_option_by_label_text(label_text, text_to_do).click()
                self.wait_until_jquery(5)
            elif action == "input":
                self.sendkeys_by_label_text(label_text, text_to_do)
            elif action == "fx":
                if len(act[1]) == 3:
                    num = act[1][2]
                else:
                    num = 0
                self.get_fx_element_by_label_text(label_text, num).click()
                self.driver.find_element_by_xpath("(//div[@class='module-tab'])[last()]").clear()
                self.driver.find_element_by_xpath("(//div[@class='module-tab'])[last()]").send_keys(text_to_do)
                self.driver.find_element_by_xpath("(//span[@class='ui-button-text'][text()='Ок'])[last()]").click()
                self.wait_until_jquery(5)
            elif action == "checkbox_weight_code":
                element = self.driver.find_element_by_xpath(
                    "//label[normalize-space(text()) = '"+act[1][0]+"']/..//input[not(@type = 'hidden')]")
                element_id = element.get_attribute("value")
                element.click()
                self.driver.find_element_by_css_selector("input[name='ShieldModel[panelWeight]["+element_id+"]']")\
                    .send_keys(act[1][1])
                self.driver.find_element_by_css_selector("input[data-id='"+element_id+"'][type='text']")\
                    .send_keys(act[1][2])
                self.driver.find_elements_by_xpath("//ul[contains(@class, 'ui-autocomplete')]"
                                                   "[contains(@style, 'display: block')]"
                                                   "//a[contains(text(),'"+act[1][2]+"')]")[0].click()
            elif action == "radio":
                element = self.driver.\
                    find_element_by_xpath("//label[text()='"+label_text+"']/..//label[text()='"+text_to_do+"']")
                element_id = element.get_attribute("for")
                self.driver.find_element_by_id(element_id).click()
            elif action == "version":
                self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
                for v in act[1]:
                    self.driver.find_element_by_xpath("//label[contains(text(), '"+v+"')]").click()
            elif action == "region":
                self.driver.find_element_by_xpath("//a[contains(text(), 'Регион')]").click()
                for v in act[1]:
                    self.driver.find_element_by_xpath("//span[text()='"+v+"']/../input").click()

        def get_element_by_label_text(self, label_text):
            element = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '"+label_text+"']/../..//input[not(@type = 'hidden')]")
            return element

        def get_elements_by_label_text(self, label_text):
            elements = self.driver.find_elements_by_xpath("//label[text() = '" +
                                                          label_text+"']/..//input[not(@type = 'hidden')]")
            return elements

        def get_fx_element_by_label_text(self, label_text, n):
            element = self.driver.find_elements_by_xpath("//label[normalize-space(text()) = '"+label_text+"']/..//a")[n]
            return element

        def sendkeys_by_label_text(self, label_text, text_to_type):
            element = self.get_element_by_label_text(label_text)
            element.clear()
            element.send_keys(text_to_type)

        def get_option_by_label_text(self, label_text, option):
            return self.driver.find_element_by_xpath("//label[normalize-space(text()) = '" +
                                                     label_text+"']/..//select/option[text() = '"+option+"']")

        def get_checkbox_by_label_text(self, label_text):
            return self.get_element_by_label_text(label_text)

        def get_input_by_label_text(self, label_text):
            return self.get_element_by_label_text(label_text)

        def click_checkbox_by_label_text(self, label_text):
            element = self.get_element_by_label_text(label_text)
            if element.is_selected():
                print label_text+" is already selected"
            else:
                element.click()

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
                element = self.get_input_by_label_text(label_text)
                return element.get_attribute("value").strip() == text_to_do.strip()
            if action == "option":
                # res = self.get_option_by_label_text(label_text, text_to_do).is_selected()
                # print "option = %s" % res
                return self.get_option_by_label_text(label_text, text_to_do).is_selected()
            if action == "fx":
                if len(param[1]) == 3:
                    num = param[1][2]
                else:
                    num = 0
                # val = self.get_elements_by_label_text(label_text)[num].get_attribute("value").strip()
                # print "fx: val = %s, text_to_do = %s" % (val, text_to_do)
                return self.get_elements_by_label_text(label_text)[num].get_attribute("value").strip() == text_to_do
            if action == "checkbox_weight_code":
                chkbox = self.driver.find_element_by_xpath(
                    "//label[normalize-space(text()) = '"+param[1][0]+"']/..//input[not(@type = 'hidden')]")
                element_id = chkbox.get_attribute("value")
                weight_input_val = \
                    self.driver.find_element_by_css_selector("input[name='ShieldModel[panelWeight]["+element_id+"]']")\
                        .get_attribute("value")
                code_input_val = \
                    self.driver.find_element_by_css_selector("input[data-id='"+element_id+"'][type='text']")\
                    .get_attribute("value")
                result = chkbox.is_selected() and weight_input_val in param[1][1] and code_input_val in param[1][2]
                return result
            if action == "radio":
                element = self.driver.\
                    find_element_by_xpath("//label[text()='"+label_text+"']/..//label[text()='"+text_to_do+"']")
                element_id = element.get_attribute("for")
                # res = self.driver.find_element_by_id(element_id).is_selected()
                # print "radio = %s" % res
                return self.driver.find_element_by_id(element_id).is_selected()
            if action == "version":
                self.driver.find_element_by_xpath("//a[contains(text(), 'Версия')]").click()
                result = True
                for v in param[1]:
                    el_id = self.driver.find_element_by_xpath("//label[contains(text(), '"+v+"')]").get_attribute("for")
                    result = result and self.driver.find_element_by_id(el_id)\
                        .is_selected()
                return result
            if action == "region":
                self.driver.find_element_by_xpath("//a[contains(text(), 'Регион')]").click()
                result = True
                for v in param[1]:
                    el = self.driver.find_element_by_xpath("//span[text()='"+v+"']/../input")
                    result = result and el.is_selected()
                return result

        def choose_nth_item(self, n):
            self.driver.find_elements_by_css_selector("a.update")[n].click()


class Group(ConstructorElement):

        item_type = "group"


class Analog(ConstructorElement):

        item_type = "analog"

        def add_group(self):
            self.driver.execute_script("$('#add-"+self.item_type+"-group').dialog('open');")  # open dialog add group
            element_text = self.choose_random_group()
            return element_text

        def choose_random_group(self):
            group_num = random.randrange(0, 10)
            element_text = self.driver.find_elements_by_css_selector("#popupGroups td:nth-of-type(1)")[group_num].text
            self.driver.find_elements_by_css_selector("#popupGroups a")[group_num].click()
            self.wait_until_jquery(5)
            return element_text

        def add_element(self, element_params, element_name="", selector="a[href$='addElement']"):
            self.driver.execute_script("$('#dictionary-nomenclature').dialog('open'); return false;")
            element_text = self.choose_random_element_from_dict()
            self.wait_until_jquery(5)
            return element_text


class Shield(ConstructorElement):

        item_type = "shield"

        def add_group(self, shield_name, params_list, add_new_product=0):
            self.driver.find_element_by_css_selector("a[href$='addGroup']").click()
            self.driver.find_element_by_css_selector("#ShieldGroupModel_title").clear()
            self.driver.find_element_by_css_selector("#ShieldGroupModel_title").send_keys(shield_name)
            self.driver.find_element_by_css_selector(".autocompleteProducts").click()
            self.driver.find_element_by_css_selector(".autocompleteProducts").send_keys("RSD 02")
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

            checkbox_text = 'Цех'
            self.driver.find_element_by_css_selector('.ui-multiselect').click()
            self.driver.find_element_by_xpath("//label/span[.='%s']/../input" % checkbox_text).click()
            self.wait_until_jquery(10)

            # if add_new_product:
            #     self.driver.find_element_by_css_selector("#addInputAutoComplete").click()
            #     self.driver.find_elements_by_css_selector("input[name='productField']")[-1].send_keys("Новое изделие")
            #     self.driver.find_elements_by_css_selector("input[name='productField']")[-1].click()
            #     self.driver.find_element_by_xpath("//a[text()='Новое изделие']").click()

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
            # self.driver.back()
            self.driver.find_element_by_css_selector(".btn-white a").click()
            return result

        def have_item(self, item_name):
            el = self.driver.find_elements_by_xpath("//a[text()='"+item_name+"']")
            return len(el) == 1

        def delete_group(self, group_name):
            delete_btn = self.driver.find_element_by_xpath(
                "//a[text()='"+group_name+"']/..//a[@class='shield-group-action delete']")
            # delete_btn_id = self.driver.find_element_by_xpath("//a[text()='"+group_name+"']").get_attribute("data-id")
            delete_btn.click()
            # delete_url_to_post = self.driver.current_url + "/deleteGroup"
            # delete_js = "$.post('"+delete_url_to_post+"',{id:'"+delete_btn_id+"',ajax:'shield-group-list'} );"
            # self.driver.execute_script(delete_js)
            alert = self.driver.switch_to_alert()
            alert.accept()
            # import time
            # time.sleep(2)
            # self.driver.refresh()
            self.wait_until_jquery(10)
            self.driver.implicitly_wait(2)

        def add_shield(self, params_list):
            self.driver.find_element_by_css_selector("#add_shield").click()
            self.update_shield(params_list)

        def update_shield(self, params_list):
            for param in params_list:
                self.do_action(param)

            self.driver.find_element_by_css_selector("#yt0").click()

        def choose_group(self, group_name):
            self.driver.find_element_by_xpath("//a[contains(@class,'shield-group')][text()='%s']" % group_name).click()

        def shield_has_params(self, params_list):
            result = all(self.check_params_on_page(param) for param in params_list)
            # self.driver.back()
            self.driver.find_element_by_css_selector(".btn-white a").click()
            return result

        def delete_added_element(self):
            delete_btn = self.driver.find_element_by_css_selector(".tbl a.delete")
            delete_btn.click()

            alert = self.driver.switch_to_alert()
            alert.accept()
            self.wait_until_jquery(5)
            import time
            time.sleep(3)


class Embedded(ConstructorElement):

        item_type = "embedded"

        def choose_kalitka_type(self):
            self.driver.find_element_by_xpath("//span[text()='Калитки']").click()
            self.wait_until_jquery(5)

        def choose_window_type(self):
            self.driver.find_element_by_xpath("//span[text()='Окна']").click()
            self.wait_until_jquery(5)

        def add_embedded_element(self, embedded_name, params_list):
            element_text = self.add_element(params_list, embedded_name)
            return element_text

        def update_element_params(self, params_list):
            self.driver.find_element_by_css_selector(".autocompleteProducts").clear()
            self.driver.find_element_by_css_selector(".autocompleteProducts").send_keys("RSD 02")
            self.driver.find_element_by_css_selector(".autocompleteProducts").click()
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

            for param in params_list:
                self.do_action(param)

            self.driver.find_element_by_css_selector("#productField").clear()
            self.driver.find_element_by_css_selector("#productField").send_keys("RSD 02")
            self.driver.find_element_by_css_selector("#productField").click()
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

            self.driver.find_element_by_xpath("//a[contains(text(), 'Карты вывода')]").click()
            for_attr = self.driver.find_element_by_xpath("//label[.='Цех']").get_attribute('for')
            self.driver.find_element_by_id(for_attr).click()

            self.driver.find_element_by_css_selector("#embeddedAdd").click()
            self.wait_until_jquery(5)

        def embedded_has_params(self, params_list):
            result = all(self.check_params_on_page(param) for param in params_list)
            self.driver.find_element_by_css_selector("#embeddedAdd").click()
            return result

        def get_element_by_label_text(self, label_text):
            element_id = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '"+label_text+"']").get_attribute('for')
            return self.driver.find_element_by_id(element_id)


class Driver(ConstructorElement):

        item_type = "driver"
        driver_type = None
        element_text = None
        subelement_text = None

        def add_driver(self, params_list, driver_type):
            self.driver_type = driver_type
            self.element_text = self.add_element(params_list)

        def update_element_params(self, params_list):
            self.driver.find_element_by_css_selector(".autocompleteProducts").click()
            self.driver.find_element_by_css_selector(".autocompleteProducts").clear()
            self.driver.find_element_by_css_selector(".autocompleteProducts").send_keys("RSD 02")
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

            checkbox_text = 'Цех'
            self.driver.find_element_by_css_selector('.ui-multiselect').click()
            self.driver.find_element_by_xpath("//label/span[.='%s']/../input" % checkbox_text).click()
            self.wait_until_jquery(10)

            self.choose_driver_type()
            if params_list:
                self.add_nomenclature_element()

                for param in params_list:
                    self.do_action(param)

                self.driver.find_element_by_css_selector("#submitButtonDriverSet").click()

            self.driver.find_element_by_css_selector("#submitButton").click()
            self.wait_until_jquery(5)

        def choose_driver_type(self, tpe=""):
            xpath_select_with_id = "//select[@id='NomenclatureDriverElementsModel_type_id']"
            if tpe:
                self.driver_type = tpe
            self.driver.find_element_by_xpath(xpath_select_with_id+"/option[text()='"+self.driver_type+"']").click()

            if tpe:
                self.driver.find_element_by_css_selector("#submitButton").click()

        def add_nomenclature_element(self):
            self.driver.find_element_by_css_selector("#addElementButton").click()

            import time
            time.sleep(5)

            self.driver.find_element_by_css_selector(".driver-btn a").click()

            self.subelement_text = self.choose_random_element_from_dict()
            self.driver.find_element_by_css_selector(".autocompleteProducts").click()
            self.driver.find_element_by_css_selector(".autocompleteProducts").clear()
            self.driver.find_element_by_css_selector(".autocompleteProducts").send_keys("RSD 02")
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

        def have_driver(self):
            self.wait_until_title_is_equal(5, "Doorhan - Приводы")
            element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(4)")[0]
            return self.element_text == element.text

        def have_driver_type(self):
            selected_option = self.driver.find_element_by_css_selector(
                "select#NomenclatureDriverElementsModel_type_id option[selected]")
            return selected_option.text == self.driver_type

        def have_subdriver(self):
            subel_text = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(3)")[0].text
            self.driver.find_element_by_css_selector("a[href*='/driver/']").click()
            # self.driver.find_element_by_css_selector("div.btn.btn-white").click()
            return self.subelement_text == subel_text

        def to_update_driver(self):
            self.driver.find_element_by_css_selector("a.update").click()

        def to_update_subdriver(self):
            self.driver.find_element_by_css_selector("a[title='Update']").click()

        def delete_driver(self):
            self.driver.find_elements_by_css_selector("tbody input")[0].click()
            self.driver.find_element_by_css_selector("#listSubmit").click()


class NomenclatureAdditional(ConstructorElement):

        item_type = "nomenclatureAdditional"
        element_text = None

        def add_nom_element(self, params_list):
            self.element_text = self.add_element(params_list, selector="a[href*='add']")

        def update_element_params(self, params_list):
            self.driver.find_element_by_css_selector(".autocompleteProducts").click()
            self.driver.find_element_by_css_selector(".autocompleteProducts").clear()
            self.driver.find_element_by_css_selector(".autocompleteProducts").send_keys("RSD 02")
            self.driver.find_element_by_xpath("//a[text()='RSD 02']").click()

            checkbox_text = 'Цех'
            self.driver.find_element_by_css_selector('.ui-multiselect').click()
            self.driver.find_element_by_xpath("//label/span[.='%s']/../input" % checkbox_text).click()

            self.wait_until_text_present(10, (By.CSS_SELECTOR, "select[id*=ProductModel_0_specification_id]"), " ")
            self.update_nom_element(params_list)

        def update_nom_element(self, params_list):
            for param in params_list:
                self.do_action(param)
            self.save_element()

        def save_element(self):
            self.driver.find_element_by_css_selector("#yt2").click()

        def sendkeys_by_label_text(self, label_text, text_to_type):
            element = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '"+label_text+"']/../..//input")
            element.clear()
            element.send_keys(text_to_type)

        def get_fx_element_by_label_text(self, label_text, n):
            xpath = ""
            if "edit" in self.driver.current_url:
                xpath = "//label[normalize-space(text()) = '"+label_text+"']/..//a"
            elif "add" in self.driver.current_url:
                xpath = "//span[normalize-space(text()) = '"+label_text+"']/..//a"
            element = self.driver.find_elements_by_xpath(xpath)[n]
            return element

        def have_nom_element(self):
            self.wait_until_title_is_equal(10, "Doorhan - Дополнительная комплектация")
            element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(4)")[0]
            return self.element_text == element.text

        def to_update_nom_element(self):
            self.driver.find_element_by_css_selector("a.update").click()

        def delete_nom_element(self):
            self.driver.find_elements_by_css_selector("tbody input")[0].click()
            self.driver.find_element_by_css_selector("#listSubmit").click()

        def nom_element_has_params(self, params_list):
            result = all(self.check_params_on_page(param) for param in params_list)

            self.driver.find_element_by_css_selector(".btn-white a").click()
            return result

        def get_input_by_label_text(self, label_text):
            return self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '"+label_text+"']/../..//input")


class AdditionalMaterial(NomenclatureAdditional):

        item_type = "nomenclatureAdditionalMaterial"
        element_text = None

        def have_nom_element(self):
            self.wait_until_title_is_equal(5, "Doorhan - Дополнительные материалы")
            element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(4)")[0]
            return self.element_text == element.text


class DriverSet(NomenclatureAdditional):

        item_type = "driverSet"
        element_text = None

        def have_nom_element(self):
            self.wait_until_title_is_equal(15, "Doorhan - Комплектация привода")
            element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(4)")[0]
            return self.element_text == element.text


class Service(NomenclatureAdditional):

        item_type = "service"
        element_text = None

        def have_nom_element(self):
            self.wait_until_title_is_equal(15, "Doorhan - Услуги")
            if len(self.driver.find_elements_by_css_selector("tbody td")) == 1:
                return False
            else:
                element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(4)")[0]
                return self.element_text == element.text


class Color(ConstructorElement):

        item_type = "colors"
        element_text = None

        def add_color_element(self, params_list):
            self.element_text = params_list[0][1][1]
            self.driver.find_element_by_css_selector("a[href$='create']").click()

            self.update_color_element(params_list)

        def save_color_element(self):
            self.driver.find_element_by_css_selector("#submitButton").click()

        def update_color_element(self, params_list):
            for param in params_list:
                self.do_action(param)

            self.save_color_element()

        def have_color_element(self):
            element = self.driver.find_elements_by_css_selector("tbody td:nth-of-type(2)")[0]
            return self.element_text.strip() == element.text.strip()

        def to_update_color_element(self):
            self.driver.find_element_by_css_selector("a.update").click()

        def delete_color_element(self):
            self.driver.find_elements_by_css_selector("tbody input")[0].click()
            self.driver.find_element_by_css_selector("#listSubmit").click()

        def color_element_has_params(self, params_list):
            result = all(self.check_params_on_page(param) for param in params_list)

            self.driver.find_element_by_css_selector(".btn-white a").click()
            return result

        def get_element_by_label_text(self, label_text):
            element = self.driver.find_element_by_xpath(
                "//label[normalize-space(text()) = '"+label_text+"']/..//input[not(@type = 'hidden')]")
            return element
