import time

import allure
import pytest
from selenium.webdriver.common.by import By

from extensions.verifications import Verifications as ver
from utilities.common_ops import wait, For, read_csv, get_data, csv_to_dictionary
from workflows.web_flows import Web_Flows as flow


@pytest.mark.usefixtures('init_web_driver_adidas')
class Test_Web_Adidas:

    def setup_method(self):
        self.driver.get(get_data('Url'))
        flow.close_cookies_pop_up()

    """"
    this test is a BUST! for some unknown reason when operating the browser with the python code the website does not
    allow an item to be added to the basket. perhaps this was done a protective measure by Adidas.
    """

    # @allure.title('Add item to bag')
    # @allure.description('Check bag number increases after adding an item to bag')
    # def test_add_to_basket(self):
    #     flow.close_cookies_pop_up()
    #     flow.open_original_shoes()
    #     flow.open_first_item()
    #     flow.add_item_to_cart()


    #This test makes use of ddt. the test should work no matter the order of the categories in the CSV(sub_category_count.csv)
    @allure.title('Test count all sub categories')
    @allure.description('Count all the sub categories of all the main categories and verify that the number is correct')
    @pytest.mark.parametrize('category,expected_result',read_csv(get_data('Sub_Category_Count_CSV')))
    def test_check_subcategory_count(self,category,expected_result):
        flow.verify_number_of_categories(category,expected_result)


    @allure.title('Test sort low to high')
    @allure.description('Sort by price "low to high" and make sure prices are arranged in that order')
    def test_sort_low_to_high(self):
        flow.open_original_shoes()
        flow.sort_low_to_high()
        flow.verify_low_to_high_prices()


    """
    This test receives a list of categories and 
    """
    @allure.title('Test filter items')
    @allure.description('Filter items by specifications and verify that the number of items is correct')
    def test_filter_by_specs(self):
        flow.open_original_shoes()
        flow.open_filter_menu()
        rows = csv_to_dictionary(get_data('Filter_Specs_CSV'))
        for row in rows:
            flow.filter_items_by_specs(row, rows[row])
        result_in_apply_button = flow.get_filter_total()
        flow.press_apply_filter_btn()
        all_items_count = flow.count_all_items_in_category()
        ver.verify_equals(result_in_apply_button, all_items_count)

    @allure.title('Test number of strips on main page')
    @allure.description('Verify that all the strips on the main page are there')
    def test_main_page_strips_exist(self):
        strip_titles = get_data('Main_Page_Strips')
        strip_titles = strip_titles.split(',')
        flow.verify_strips(strip_titles)

    @allure.title('Test search items')
    @allure.description('Search for specific items using ddt')
    def test_search_item(self):
        flow.search_item('SAMBA OG SHOES')