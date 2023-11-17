from selenium.webdriver.common.by import By

first_item_title = (By.XPATH,"//*[@id='wishListItemName'][1]")
more_options = (By.XPATH,"//*[@id='moreOptionImage'][1]")
remove_from_wishlist = (By.XPATH,"//*[@text='Remove from Wishlist']")


class App_Wishlist_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_first_item_name(self):
        return self.driver.find_element(first_item_title[0],first_item_title[1])

    def get_more_options(self):
        return self.driver.find_element(more_options[0],more_options[1])

    def get_remove_from_wishlist(self):
        return self.driver.find_element(remove_from_wishlist[0],remove_from_wishlist[1])