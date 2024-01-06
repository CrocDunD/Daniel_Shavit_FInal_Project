from selenium.webdriver.common.by import By

more_options_button = (By.XPATH,"//*[@id='more_options']")
remove_button = (By.XPATH,"//*[@id='REMOVE_text']")


class App_Basket_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_more_options_button(self):
        return self.driver.find_element(more_options_button[0],more_options_button[1])

    def get_remove_button(self):
        return self.driver.find_element(remove_button[0],remove_button[1])