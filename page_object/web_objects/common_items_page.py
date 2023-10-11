from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

first_item = (By.XPATH,'//*[@class="row product-wrapsection"]/div[1]')
all_items = (By.XPATH,'//*[@class="row product-wrapsection"]/div')
all_items_prices = (By.XPATH,'//*[@class="row product-wrapsection"]/div//div[@class="price"]/span')
sort_btn = (By.XPATH,'(//*[@aria-label="Sort by"])[1]')
low_to_high_btn = (By.XPATH,'(//*[@data-id="price-low-to-high"])[1]')
filter_button = (By.XPATH,'(//*[@class="btn filter-results col-12 m-0"])[1]')
page_drop = (By.XPATH,'//select[@class="form-control custom-select plp-pagecount-select"][1]')
last_page = (By.XPATH,'//*[@class="pageofNumber"]')
loader_anim = (By.XPATH,'//*[@class="gl-loader"]')



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

    def get_filter_button(self):
        return self.driver.find_element(filter_button[0],filter_button[1])

    def get_page_drop(self):
        return Select(self.driver.find_element(page_drop[0],page_drop[1]))

    def get_last_page_number(self):
        return self.driver.find_element(last_page[0],last_page[1])

    def get_loader_anim(self):
        return self.driver.find_element(loader_anim[0],loader_anim[1])