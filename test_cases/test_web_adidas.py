import time

import allure
import pytest
from selenium.webdriver.common.by import By

from utilities.common_ops import wait, For, read_csv, get_data
from workflows.web_flows import Web_Flows as flow


@pytest.mark.usefixtures('init_web_driver_adidas')
class Test_Web_Adidas:

    @allure.title('Add item to bag')
    @allure.description('Check bag number increases after adding an item to bag')
    def test_add_to_basket(self):
        flow.close_cookies_pop_up()
        flow.open_original_shoes()
        flow.open_first_item()
        flow.add_item_to_cart()

    #This test makes use of ddt. the test should work no matter the order of the categories in the CSV(sub_category_count.csv)
    @allure.title('Test count all sub categories')
    @allure.description('Count all the sub categories of all the main categories and verify that the number is correct')
    @pytest.mark.parametrize('category,expected_result',read_csv(get_data('Sub_Category_Count_CSV')))
    def test_check_subcategory_count(self,category,expected_result):
        flow.close_cookies_pop_up()
        flow.verify_number_of_categories(category,expected_result)


    @allure.title('Test sort low to high')
    @allure.description('Sort by price "low to high" and make sure prices are arranged in that order')
    def test_sort_low_to_high(self):
        flow.close_cookies_pop_up()
        flow.open_original_shoes()
        flow.sort_low_to_high()
        time.sleep(3)
        flow.verify_low_to_high_prices()



    #verify that all the strips on the main page are there

    #search for a specific item using ddt

    #sort by price low to high and make sure prices are arranged in that order

    #filter a list of items and verify that the number in the search button is equal to the count of items seen