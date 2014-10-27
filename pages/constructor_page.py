# coding=utf-8
from __future__ import unicode_literals
from base_page import BasePage
from items.nomenclature_additional_material_item import NomenclatureAdditionalMaterial
from items.nomenclature_additional_item import NomenclatureAdditional
from items.driver_item import Driver
from items.driver_set_item import DriverSet
from items.service_item import Service
from items.color_item import Color
from items.embedded_item import Embedded
from items.analog_item import Analog
from items.group_item import Group
from items.shield_item import Shield


class ConstructorPage(BasePage):

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

    def navigate_nomenclature_additional_material(self):
        self.navigate_item("nomenclatureAdditionalMaterial")
        return NomenclatureAdditionalMaterial(self.driver)

    def navigate_driver_set(self):
        self.navigate_item("driverSet")
        return DriverSet(self.driver)

    def navigate_service(self):
        self.navigate_item("service")
        return Service(self.driver)

    def navigate_color(self):
        self.navigate_item("colors")
        return Color(self.driver)

    def navigate_item(self, item_type):
        item_url = ''.join([self.url, 'constructor/', item_type])
        self.driver.get(item_url)