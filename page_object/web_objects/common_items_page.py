from selenium.webdriver.common.by import By

first_item = (By.XPATH,'//*[@class="row product-wrapsection"]/div[1]')
all_items = (By.XPATH,'//*[@class="row product-wrapsection"]/div')
all_items_prices = (By.XPATH,'//*[@class="row product-wrapsection"]/div//div[@class="price"]/span')
sort_btn = (By.XPATH,'(//*[@aria-label="Sort by"])[1]')
low_to_high_btn = (By.XPATH,'(//*[@data-id="price-low-to-high"])[1]')


class Common_Items_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_first_item(self):
        return self.driver.find_element(first_item[0],first_item[1])

    def get_all_items(self):
        return self.driver.find_elements(all_items[0],all_items[1])

    def get_all_item_prices(self):
        raw_prices =  self.driver.find_elements(all_items_prices[0],all_items_prices[1])
        real_prices = []
        for price in raw_prices:
            real_price = float(price.find_element(By.XPATH,'span/span').get_attribute('content'))
            real_prices.append(real_price)
        return real_prices


    def get_sort_btn(self):
        return self.driver.find_element(sort_btn[0],sort_btn[1])

    def get_low_to_high_btn(self):
        return self.driver.find_element(low_to_high_btn[0],low_to_high_btn[1])