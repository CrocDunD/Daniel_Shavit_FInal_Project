from selenium.webdriver.common.by import By

item_title = (By.XPATH,"//*[@id='tvProductName']")
drawer_line = (By.XPATH, "//*[@id='ivDrawer']")
back_btn = (By.XPATH, "//*[@id='imgToolbarBack']")
select_size_btn = (By.XPATH, "//*[@id='anchoredButton']")
add_to_bag_btn = (By.XPATH, "//*[@id='btnAddToCart']")
view_bag_btn = (By.XPATH, "//*[@id='pdp_view_cart_button']")


class Product_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_item_title(self):
        return self.driver.find_element(item_title[0],item_title[1])


    def get_drawer_line(self):
        return self.driver.find_element(drawer_line[0],drawer_line[1])

    def get_back_btn(self):
        return self.driver.find_element(back_btn[0],back_btn[1])

    def get_select_size(self):
        return self.driver.find_element(select_size_btn[0],select_size_btn[1])

    def get_add_to_bag_btn(self):
        return self.driver.find_element(add_to_bag_btn[0],add_to_bag_btn[1])

    def get_view_bag_btn(self):
        return self.driver.find_element(view_bag_btn[0],view_bag_btn[1])

