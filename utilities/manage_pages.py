import test_cases
from page_object.app_objects.app_basket_page import App_Basket_Page
from page_object.app_objects.app_login_page import App_Login_Page
from page_object.app_objects.app_navbar_page import App_Navbar_Page
from page_object.app_objects.app_profile_page import App_Profile_Page
from page_object.app_objects.app_wishlist_page import App_Wishlist_Page
from page_object.app_objects.app_drops_page import  Drops_Page
from page_object.app_objects.app_product_page import  Product_Page
from page_object.app_objects.app_shop_page import Shop_Page
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

app_drops_page = None
app_shop_page = None
app_product_page = None
app_navbar_page = None
app_login_page = None
app_profile_page = None
app_wishlist_page = None
app_basket_page = None

class Manage_Pages:
    @staticmethod
    def init_web_pages():
        global web_front_page, web_common_items_page, web_navbar_page, web_item_page, web_filter_page

        web_front_page = Front_Page(test_cases.conftest.driver)
        web_common_items_page = Common_Items_Page(test_cases.conftest.driver)
        web_navbar_page = Navbar_Page(test_cases.conftest.driver)
        web_item_page = Item_Page(test_cases.conftest.driver)
        web_filter_page = Filter_Page(test_cases.conftest.driver)

    @staticmethod
    def init_app_pages():
        global app_drops_page, app_shop_page, app_product_page, app_navbar_page, app_login_page, app_profile_page, app_wishlist_page, app_basket_page

        app_drops_page = Drops_Page(test_cases.conftest.driver)
        app_shop_page = Shop_Page(test_cases.conftest.driver)
        app_product_page = Product_Page(test_cases.conftest.driver)
        app_navbar_page = App_Navbar_Page(test_cases.conftest.driver)
        app_login_page = App_Login_Page(test_cases.conftest.driver)
        app_profile_page = App_Profile_Page(test_cases.conftest.driver)
        app_wishlist_page = App_Wishlist_Page(test_cases.conftest.driver)
        app_basket_page = App_Basket_Page(test_cases.conftest.driver)
