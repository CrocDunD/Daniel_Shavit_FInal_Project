import time

import allure
from selenium.webdriver.common.by import By

from page_object.web_objects.common_items_page import last_page, all_items, loader_anim
from page_object.web_objects.front_page import X_btn_first_popup
from page_object.web_objects.navbar_page import men_category_drop, main_category
from page_object.web_objects.item_page import add_to_cart_btn
from utilities.common_ops import read_csv, get_data, For, lower_strip_list
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
                wait(For.ELEMENT_DISPLAYED,X_btn_first_popup)
                Ui_Actions.click(page.web_front_page.get_X_btn_first_popup())
            if page.web_front_page.get_close_join_club().is_displayed():
                Ui_Actions.click(page.web_front_page.get_close_join_club())
        except:
            pass


    @staticmethod
    @allure.step('Go to original shoes category')
    def open_original_shoes():
        wait(For.ELEMENT_DISPLAYED,men_category_drop)
        time.sleep(2)
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
                break
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
        wait(For.ELEMENT_INVISIBLE, loader_anim)
        prices = page.web_common_items_page.get_all_item_prices()
        ver.soft_assert_first_smaller_than_second(prices)

    @staticmethod
    @allure.step('Open filter menu')
    def open_filter_menu():
        Ui_Actions.click(page.web_common_items_page.get_filter_button())

    @staticmethod
    @allure.step('Filter items by specifications')
    def filter_items_by_specs(categories_to_filter: str, choices_to_filter: list):
        lower_strip_list(choices_to_filter)

        for x in range(len(choices_to_filter)):
            filter_num = 0
            all_categories = page.web_filter_page.get_filter_options()

            for category in all_categories:
                cat_text = category.find_element(By.XPATH, 'div/button/span').text.lower().strip()
                if cat_text == categories_to_filter.lower().strip():
                    correct_category = category.find_element(By.XPATH,'div/button')
                    if 'active' in category.get_attribute('class'):
                        pass
                    else:
                        Ui_Actions.click(correct_category)
                    filter_num += 1
                    break
                filter_num += 1

            counter = 0
            while len(choices_to_filter) > 0:

                all_choices = page.web_filter_page.get_all_filter_options(filter_num)
                elem = all_choices[counter]
                choice_text = elem.find_element(By.XPATH,'a/span').text.lower().strip()
                if choice_text in choices_to_filter:
                    choices_to_filter.remove(choice_text)
                    Ui_Actions.click(elem)
                    wait(For.ELEMENT_INVISIBLE, loader_anim)
                    break
                counter += 1



    @staticmethod
    @allure.step('Get filter total')
    def get_filter_total():
        return int((page.web_filter_page.get_filter_result_count().text.strip())[1:-1])

    @staticmethod
    @allure.step('Press the apply filter button')
    def press_apply_filter_btn():
        Ui_Actions.click(page.web_filter_page.get_filter_apply_btn())

    @staticmethod
    @allure.step('Count all items in category')
    def count_all_items_in_category():
        wait(For.ELEMENT_INVISIBLE, loader_anim)
        if len(page.web_common_items_page.get_last_page_number()) > 0:
            last_page_number = int(page.web_common_items_page.get_last_page_number()[0].text[3:])
            page_drop = page.web_common_items_page.get_page_drop()
            page_drop.select_by_index(last_page_number-1)
            wait(For.ELEMENT_INVISIBLE, loader_anim)
            items_in_all_pages_but_last = 24 * (last_page_number - 1)
            items_in_last_page = len(page.web_common_items_page.get_all_items())
            return items_in_all_pages_but_last + items_in_last_page
        else:
            items_in_last_page = len(page.web_common_items_page.get_all_items())
            return items_in_last_page
    @staticmethod
    @allure.step('Verify all strips')
    def verify_strips(strip_list):
        strip_elems = []
        for strip in strip_list:
            elem = page.web_front_page.get_strip_element_by_text(strip)
            strip_elems.append(elem)
        ver.soft_displayed(strip_elems)

    @staticmethod
    @allure.step('verify search item')
    def search_item(item_name: str):
        Ui_Actions.update_text(page.web_navbar_page.get_search_field(),item_name)
        wait(For.ELEMENT_INVISIBLE, loader_anim)
        Ui_Actions.click(page.web_navbar_page.get_search_drop_menu_first_item())
        item_title = page.web_item_page.get_item_title().text.lower().strip()
        assert item_title == item_name.strip().lower()