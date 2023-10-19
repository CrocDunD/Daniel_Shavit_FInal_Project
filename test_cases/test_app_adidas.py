import time

import pytest

from utilities.common_ops import get_data
from workflows.app_flows import App_Flows as flow


@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_App_Adidas:

    def test_search_for_item(self):
        item_name = get_data('Item_Search').strip().lower()
        title = flow.search_for_something(item_name)
        assert title.strip().lower() == item_name




    #search for a specific item store in data.xml

    #add item to basket

    #change order of front page banners

    #add item to wishlist