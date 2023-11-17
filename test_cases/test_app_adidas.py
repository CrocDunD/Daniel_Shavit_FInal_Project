import time

import allure
import pytest

from utilities.common_ops import get_data
from workflows.app_flows import App_Flows as flow
from extensions.verifications import Verifications as ver



@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_App_Adidas:

    #def setup_method(self):
    #    flow.go_to_navbar(2)

    allure.title('Search Item')
    allure.step('Test search of an item and and verifying the title is correct')
    def test_search_for_item(self):
        item_name = get_data('Item_Search').strip().lower()
        title = flow.search_for_something(item_name)
        assert title.strip().lower() == item_name


    allure.title('Add Item To Basket')
    allure.step('Test adding an item to the basket and verifying that the basket total is increased')
    def test_add_item_to_basket(self):
        items_total_before = int(flow.get_item_bag_total())
        flow.go_to_mens_category()
        flow.go_to_first_category()
        flow.go_to_first_sub_category()
        flow.go_to_first_item()
        flow.add_to_bag_and_go_to_bag()
        items_total_after = int(flow.get_item_bag_total())
        ver.verify_equals(items_total_before + 1, items_total_after)

    allure.title('Login With Email')
    allure.step('Test Logging in to a user with an email')

    def test_login_email(self):
        flow.click_profile_btn()
        profile_title = flow.login_with_email_flow('daniels@inmanage.net', get_data('AppPassWord'))
        ver.is_displayed(profile_title)


    allure.title('Change Order of Page Banners')
    allure.step('Test changing the order of the the "Recommended for You" section')
    def test_change_banner_order(self):
        flow.go_to_navbar(1)
        time.sleep(3)
        flow.swipe()


    allure.title('Add Item To Wishlist')
    allure.step('Test adding an item to the wishlist and verifying that it has in fact been added')
    def test_add_to_wishlist(self):
        flow.go_to_mens_category()
        flow.go_to_first_category()
        flow.go_to_first_sub_category()
        product_name = flow.wishlist_item().lower()
        flow.go_to_navbar(3)
        name_in_wishlist = flow.get_first_wishlist_item_name().lower()
        flow.remove_wishlist_item()
        ver.verify_equals(product_name, name_in_wishlist)