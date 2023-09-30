from selenium.webdriver.common.by import By

first_item = (By.XPATH,'//*[@class="row product-wrapsection"]/div[1]')
sort_btn = (By.XPATH,'(//*[@aria-label="Sort by"])[1]')
low_to_high_btn = (By.XPATH,'(//*[@data-id="price-low-to-high"])[1]')

class Common_Items_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_first_item(self):
        return self.driver.find_element(first_item[0],first_item[1])

    def get_sort_btn(self):
        return self.driver.find_element(sort_btn[0],sort_btn[1])

    def get_low_to_high_btn(self):
        return self.driver.find_element(low_to_high_btn[0],low_to_high_btn[1])