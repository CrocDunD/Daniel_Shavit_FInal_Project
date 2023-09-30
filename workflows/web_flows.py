import time

import allure
from selenium.webdriver.common.by import By

from page_object.web_objects.item_page import add_to_cart_btn
from utilities.common_ops import read_csv, get_data, For
from utilities import manage_pages as page
from extensions.ui_actions import Ui_Actions
from utilities.common_ops import wait
from extensions.verifications import Verifications as ver


class Web_Flows:

    @staticmethod
    @allure.step('Close cookies pop up')
    def close_cookies_pop_up():
        try:
            if page.web_front_page.get_X_btn_first_popup().is_displayed():
                Ui_Actions.click(page.web_front_page.get_X_btn_first_popup())
        except:
            pass

    @staticmethod
    @allure.step('Go to original shoes category')
    def open_original_shoes():
        Ui_Actions.mouse_hover_and_click(page.web_navbar_page.get_men_category(), page.web_navbar_page.get_original_shoes_btn())

    @staticmethod
    @allure.step('Open first item') #opens first item out of a list of products
    def open_first_item():
        Ui_Actions.click(page.web_common_items_page.get_first_item())

    @staticmethod
    @allure.step('Add item to cart from item page')
    def add_item_to_cart():
        Ui_Actions.click(page.web_item_page.get_available_size())
        #wait(For.ELEMENT_EXISTS,add_to_cart_btn)
        Ui_Actions.click(page.web_item_page.get_add_to_cart_btn())


    @staticmethod
    @allure.step('Verify number of sub categories')
    def verify_number_of_categories(category,expected_categories):
        main_cats = page.web_navbar_page.get_main_category()
        relevant_cat = None
        for x in main_cats:
            if x.text.lower() == category.lower():
                relevant_cat = x
                pass
        Ui_Actions.mouse_hover(relevant_cat)
        actual_categories = page.web_navbar_page.get_number_of_sub_categories(relevant_cat)
        ver.verify_equals(str(actual_categories), expected_categories.strip())

    @staticmethod
    @allure.step('change to sort by low to high')
    def sort_low_to_high():
        Ui_Actions.click(page.web_common_items_page.get_sort_btn())
        Ui_Actions.click(page.web_common_items_page.get_low_to_high_btn())

    @staticmethod
    @allure.step('Verify low to high prices')
    def verify_low_to_high_prices():
        prices = page.web_common_items_page.get_all_item_prices()
        ver.soft_assert_fisrt_smaller_than_second(prices)


