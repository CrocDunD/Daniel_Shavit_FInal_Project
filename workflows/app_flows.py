import time

import allure
from selenium.common.exceptions import NoSuchElementException

from extensions.ui_actions import Ui_Actions, Key
from page_object.app_objects.product_page import select_size_btn
from page_object.app_objects.shop_page import first_category, first_sub_category, first_item, men_category
from test_cases import conftest
from utilities import manage_pages as page
from utilities.common_ops import wait, For


class App_Flows:

    @staticmethod
    @allure.step('Search for something')
    def search_for_something(item_name):
        Ui_Actions.click(page.app_shop_page.get_search_field())
        Ui_Actions.click(page.app_shop_page.get_edit_text())
        Ui_Actions.update_text(page.app_shop_page.get_edit_text(), item_name)
        Ui_Actions.click_mobile_keyboard_key(Key.SEARCH)
        Ui_Actions.click(page.app_shop_page.get_first_item())
        return page.app_product_page.get_item_title().text

    @staticmethod
    @allure.step('click on a navbar button')
    def go_to_navbar():
        Ui_Actions.click(page.app_navbar_page.get_navbar_button())

    @staticmethod
    @allure.step('click on a navbar button')
    def go_to_mens_category():
        wait(For.ELEMENT_DISPLAYED,men_category)
        Ui_Actions.click(page.app_shop_page.get_men_category())

    @staticmethod
    @allure.step('click on a first category')
    def go_to_first_category():
        wait(For.ELEMENT_DISPLAYED,first_category)
        Ui_Actions.click(page.app_shop_page.get_first_category())

    @staticmethod
    @allure.step('click on a first sub category')
    def go_to_first_sub_category():
        wait(For.ELEMENT_DISPLAYED,first_sub_category)
        Ui_Actions.click(page.app_shop_page.get_first_sub_category())

    @staticmethod
    @allure.step('click on a first item in list')
    def go_to_first_item():
        wait(For.ELEMENT_DISPLAYED,first_item)
        Ui_Actions.click(page.app_shop_page.get_first_item())

    @staticmethod
    @allure.step('add to bag')
    def add_to_bag_and_go_to_bag():
        wait(For.ELEMENT_DISPLAYED,select_size_btn)
        Ui_Actions.click(page.app_product_page.get_select_size())
        Ui_Actions.click(page.app_product_page.get_add_to_bag_btn())
        Ui_Actions.click(page.app_product_page.get_view_bag_btn())

    @staticmethod
    @allure.step('get number of items in bag')
    def get_item_bag_total():
        try:
            return page.app_navbar_page.get_item_bag_total().text
        except NoSuchElementException:
            return 0
