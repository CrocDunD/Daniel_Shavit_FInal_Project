import time

import allure
from extensions.ui_actions import Ui_Actions, Key
from utilities import manage_pages as page


class App_Flows:

    @staticmethod
    @allure.step('Search for something')
    def search_for_something(item_name):
        Ui_Actions.click(page.app_shop_page.get_search_field())
        Ui_Actions.click(page.app_shop_page.get_edit_text())
        Ui_Actions.update_text(page.app_shop_page.get_edit_text(), item_name)
        Ui_Actions.click_mobile_keyboard_key(Key.SEARCH)
        Ui_Actions.click(page.app_shop_page.get_first_item())
        return page.app_product_page.get_item_title().text
