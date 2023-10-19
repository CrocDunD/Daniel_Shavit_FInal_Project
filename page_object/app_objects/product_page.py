from selenium.webdriver.common.by import By

item_title = (By.XPATH,"//*[@id='tvProductName']")


class Product_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_item_title(self):
        return self.driver.find_element(item_title[0],item_title[1])

