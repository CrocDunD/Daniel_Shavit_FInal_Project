import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from extensions.ui_actions import Ui_Actions, Key
from page_object.app_objects.app_login_page import sign_in_end_btn, login_btn, continue_arrow, editable_field
from page_object.app_objects.app_wishlist_page import first_item_title
from page_object.app_objects.app_product_page import select_size_btn
from page_object.app_objects.app_shop_page import first_category, sub_category, first_item, men_category, heart_btn
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
    @staticmethod
    @allure.step('Get Item Name')
    def get_item_name():
        return page.app_product_page.get_item_title().text

    @staticmethod
    @allure.step('click on a navbar button')
    def go_to_navbar(number):
        Ui_Actions.click(page.app_navbar_page.get_navbar_btn(number))

    @staticmethod
    @allure.step('click on a navbar button')
    def go_to_mens_category():
        wait(For.ELEMENT_DISPLAYED,men_category)
        Ui_Actions.click(page.app_shop_page.get_men_category())

    @staticmethod
    @allure.step('click on a first category')
    def go_to_category(cat):
        Ui_Actions.click(page.app_shop_page.get_first_category(cat))

    @staticmethod
    @allure.step('click on a first sub category')
    def go_to_sub_category(sub_c):
        try:
            Ui_Actions.click(page.app_shop_page.get_sub_category(sub_c))
        except:
            pass

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

    @staticmethod
    @allure.step('Click profile button')
    def click_profile_btn():
        Ui_Actions.click(page.app_navbar_page.get_profile_btn())

    @staticmethod
    @allure.step('login with email')
    def login_with_email_flow(email, password):
        #wait(For.ELEMENT_DISPLAYED, login_btn)
        time.sleep(3)
        Ui_Actions.click(page.app_login_page.get_login_btn())
        Ui_Actions.click(page.app_login_page.get_login_with_email_btn())
        Ui_Actions.clear(page.app_login_page.get_editable_field())
        Ui_Actions.update_text(page.app_login_page.get_editable_field(), email)
        wait(For.ELEMENT_DISPLAYED, continue_arrow)
        Ui_Actions.click(page.app_login_page.get_continue_arrow())
        wait(For.ELEMENT_DISPLAYED, editable_field)
        Ui_Actions.update_text(page.app_login_page.get_editable_field(), password)
        Ui_Actions.click(page.app_login_page.get_sing_in_end_btn())
        return page.app_profile_page.get_my_account_title()


    @staticmethod
    @allure.step('Wishlist item')
    def wishlist_item():
        wait(For.ELEMENT_TO_BE_CLICKABLE, heart_btn)
        product = page.app_shop_page.get_first_item()
        Ui_Actions.click(page.app_shop_page.get_heart_btn())
        return product.find_element(By.XPATH, "//*[@id='product_name']").text


    @staticmethod
    @allure.step('Get name of first wishlisted item')
    def get_first_wishlist_item_name():
        return page.app_wishlist_page.get_first_item_name().text

    @staticmethod
    @allure.step('Remove wishlisted item')
    def remove_wishlist_item():
        Ui_Actions.click(page.app_wishlist_page.get_more_options())
        Ui_Actions.click(page.app_wishlist_page.get_remove_from_wishlist())

    @staticmethod
    @allure.step('Remove basket item')
    def remove_basket_item():
        Ui_Actions.click(page.app_basket_page.get_more_options_button())
        Ui_Actions.click(page.app_basket_page.get_remove_button())

    @staticmethod
    @allure.step('swipe')
    def swipe():
        Ui_Actions.swipe()

    @staticmethod
    @allure.step('Go to front page')
    def go_to_front_page():
        conftest.driver.close_app()
        conftest.driver.launch_app()
        App_Flows.go_to_navbar(2)
        # try:
        #     App_Flows.go_to_navbar(2)
        # except:
        #     conftest.driver.press_keycode(4)
        #     App_Flows.go_to_navbar(2)
        #     while not page.app_shop_page.get_shop_title().is_displayed():
        #         conftest.driver.press_keycode(4)






