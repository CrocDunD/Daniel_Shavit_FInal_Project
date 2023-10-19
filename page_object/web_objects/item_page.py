from selenium.webdriver.common.by import By

X_btn_first_popup = (By.XPATH,'//*[@class="affirm btn btn-primary btn-inline"]')
men_category_drop = (By.XPATH,'//*[@id="men"][1]')
original_shoes_btn = (By.XPATH,'//*[@id="men-originals"][1]')
sizes_board = (By.XPATH,'//*[@class="radio-group size-tabs"]/div')
add_to_cart_btn = (By.XPATH,'//*[@class="add-to-cart btn btn-primary ready"]')
item_title = (By.XPATH,'//h1[@class="product-name hidden-sm-down"]')

class Item_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_available_size(self):
        sizes = self.driver.find_elements(sizes_board[0],sizes_board[1])
        available = None
        for x in sizes:
            if x.get_attribute('class').strip() == "size-radio":
                available = x
                pass
        return available

    def get_add_to_cart_btn(self):
        return self.driver.find_element(add_to_cart_btn[0],add_to_cart_btn[1])

    def get_item_title(self):
        return self.driver.find_element(item_title[0],item_title[1])
