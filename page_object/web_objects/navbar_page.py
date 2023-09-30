from selenium.webdriver.common.by import By

men_category_drop = (By.XPATH,'//*[@id="men"][1]')
original_shoes_btn = (By.XPATH,'//*[@id="men-originals"][1]')
mens_sub_categories = (By.XPATH,'//*[@class="nav-item dropdown has-clp show"]//ul/li/ul/li')
main_category = (By.XPATH,'(//*[@class="nav navbar-nav"])[1]/li')

class Navbar_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_men_category(self):
        return self.driver.find_element(men_category_drop[0],men_category_drop[1])

    def get_original_shoes_btn(self):
        return self.driver.find_element(original_shoes_btn[0],original_shoes_btn[1])

    def get_number_of_sub_categories(self, catagory):
        return len(catagory.find_elements(By.XPATH,'div/div/ul/li//li'))

    def get_main_category(self):
        return self.driver.find_elements(main_category[0],main_category[1])