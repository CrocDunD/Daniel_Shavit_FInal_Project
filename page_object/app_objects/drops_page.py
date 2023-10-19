from selenium.webdriver.common.by import By

search_btn = (By.XPATH, "//*[@id='browseIcon']")

class Drops_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_search_btn(self):
        return self.driver.find_element(search_btn[0],search_btn[1])