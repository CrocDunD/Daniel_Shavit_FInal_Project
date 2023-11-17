from selenium.webdriver.common.by import By

my_account_title = (By.XPATH,"//*[@text='MY ACCOUNT']")


class App_Profile_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_my_account_title(self):
        return self.driver.find_element(my_account_title[0],my_account_title[1])