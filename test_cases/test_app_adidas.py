import time

import allure
import pytest

from utilities.common_ops import get_data
from workflows.app_flows import App_Flows as flow
from extensions.verifications import Verifications as ver



@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_App_Adidas:

    def setup_method(self):
        flow.go_to_front_page()

    #This test searches for an item by product code and compares the name in the product page to an expected result
    #AppItemID and AppItemName can be edited in the data.xml file
    #Product code can be found in the specifications in the product page on the app
    allure.title('Search Item')
    allure.description('Test search of an item and and verifying the title is correct')
    def test_search_for_item(self):
        flow.search_for_something(get_data('AppItemID'))
        title = flow.get_item_name()
        ver.verify_equals(title.strip().lower(),get_data("AppItemName").strip().lower())


    allure.title('Add Item To Basket')
    allure.description('Test adding an item to the basket and verifying that the basket total is increased')
    def test_add_item_to_basket(self):
        items_total_before = int(flow.get_item_bag_total())
        item_name = get_data('AppItemID').strip().lower()
        flow.search_for_something(item_name)
        flow.add_to_bag_and_go_to_bag()
        items_total_after = int(flow.get_item_bag_total())
        flow.go_to_navbar(4)
        flow.remove_basket_item()
        ver.verify_equals(items_total_before + 1, items_total_after)


    allure.title('Login With Email')
    allure.description('Test Logging in to a user with an email')
    def test_login_email(self):
        flow.click_profile_btn()
        profile_title = flow.login_with_email_flow(get_data('AppUserName'), get_data('AppPassWord'))
        ver.is_displayed(profile_title)


    allure.title('Add Item To Wishlist')
    allure.description('Test adding an item to the wishlist and verifying that it has in fact been added')
    def test_add_to_wishlist(self):
        flow.go_to_mens_category()
        flow.go_to_category(get_data("Category"))
        flow.go_to_sub_category(get_data("SubCategory"))
        product_name = flow.wishlist_item().lower()
        flow.go_to_navbar(3)
        name_in_wishlist = flow.get_first_wishlist_item_name().lower()
        flow.remove_wishlist_item()
        ver.verify_equals(product_name, name_in_wishlist)