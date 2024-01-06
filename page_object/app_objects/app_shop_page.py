from selenium.webdriver.common.by import By

search_field = (By.XPATH,"//*[@id='search_input_field']")
edit_text = (By.XPATH,"//*[@class='android.widget.EditText']")
first_item = (By.XPATH,"//*[@id='plp_product_cell'][1]")
men_category = (By.XPATH, "//*[@id='shop_top_navigation_men']")
first_category = (By.XPATH, "(//*[@id='category-cell-category-name'])[1]")
sub_category = (By.XPATH, "//*[@text='SHOES']")
heart_btn = (By.XPATH, "(//*[@id='product_wish_list_button'])[1]")
shop_title = (By.XPATH, "//*[@text='SHOP']")
class Shop_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_search_field(self):
        return self.driver.find_element(search_field[0],search_field[1])

    def get_edit_text(self):
        return self.driver.find_element(edit_text[0],edit_text[1])

    def get_first_item(self):
        return self.driver.find_element(first_item[0],first_item[1])

    def get_men_category(self):
        return self.driver.find_element(men_category[0],men_category[1])

    def get_first_category(self, category):
        return self.driver.find_element(By.XPATH, '//*[@text="'+ category +'"]')

    def get_sub_category(self, sub_category):
        return self.driver.find_element(By.XPATH, '//*[@text="'+ sub_category +'"]')

    def get_heart_btn(self):
        return self.driver.find_element(heart_btn[0],heart_btn[1])

    def get_shop_title(self):
        return self.driver.find_element(shop_title[0],shop_title[1])



