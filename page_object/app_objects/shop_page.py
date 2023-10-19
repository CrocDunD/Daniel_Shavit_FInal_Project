from selenium.webdriver.common.by import By

search_field = (By.XPATH,"//*[@id='search_input_field']")
edit_text = (By.XPATH,"//*[@class='android.widget.EditText']")
first_item = (By.XPATH,"//*[@id='plp_product_cell'][1]")
class Shop_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_search_field(self):
        return self.driver.find_element(search_field[0],search_field[1])

    def get_edit_text(self):
        return self.driver.find_element(edit_text[0],edit_text[1])

    def get_first_item(self):
        return self.driver.find_element(first_item[0],first_item[1])
