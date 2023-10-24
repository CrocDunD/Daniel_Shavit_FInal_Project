import time

import allure
import pytest

from utilities.common_ops import get_data
from workflows.app_flows import App_Flows as flow
from extensions.verifications import Verifications as ver



@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_App_Adidas:

    #def setup_method(self):
    #    flow.go_to_navbar()

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






    #change order of front page banners

    #add item to wishlist