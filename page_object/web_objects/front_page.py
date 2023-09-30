from selenium.webdriver.common.by import By

X_btn_first_popup = (By.XPATH,'//*[@class="affirm btn btn-primary btn-inline"]')
men_category_drop = (By.XPATH,'//*[@id="men"][1]')
original_shoes_btn = (By.XPATH,'//*[@id="men-originals"][1]')

class Front_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_X_btn_first_popup(self):
        return self.driver.find_element(X_btn_first_popup[0],X_btn_first_popup[1])


