import test_cases
from page_object.web_objects.filter_page import Filter_Page
from page_object.web_objects.front_page import Front_Page
from page_object.web_objects.common_items_page import Common_Items_Page
from page_object.web_objects.item_page import Item_Page
from page_object.web_objects.navbar_page import Navbar_Page

web_front_page = None
web_common_items_page = None
web_navbar_page = None
web_item_page = None
web_filter_page = None



class Manage_Pages:
    @staticmethod
    def init_web_pages():
        global web_front_page, web_common_items_page, web_navbar_page, web_item_page, web_filter_page

        web_front_page = Front_Page(test_cases.conftest.driver)
        web_common_items_page = Common_Items_Page(test_cases.conftest.driver)
        web_navbar_page = Navbar_Page(test_cases.conftest.driver)
        web_item_page = Item_Page(test_cases.conftest.driver)
        web_filter_page = Filter_Page(test_cases.conftest.driver)

