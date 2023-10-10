from selenium.webdriver.common.by import By

filter_page = (By.XPATH,'//*[@class="refinements desktop"]')
filter_options = (By.XPATH,'//*[@class="refinements desktop"]/*')
filter_result_count = (By.XPATH,'//*[@class="sidebar-apply-button"]//span')
filter_apply_btn = (By.XPATH,'//*[@class="sidebar-apply-button"]//a')
elem2 = (By.XPATH,'/html/body/div[3]/div[1]/div[5]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[2]/ul/li[2]/a')


class Filter_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_filter_page(self):
        return self.driver.find_element(filter_page[0],filter_page[1])

    def get_filter_options(self):
        return self.driver.find_elements(filter_options[0],filter_options[1])

    def get_filter_result_count(self):
        return self.driver.find_element(filter_result_count[0],filter_result_count[1])

    def get_filter_apply_btn(self):
        return self.driver.find_element(filter_apply_btn[0],filter_apply_btn[1])

    def get_all_filter_options(self, filter_num):
        return self.driver.find_elements(By.XPATH,'//*[@class="refinements desktop"]/div[' + str(filter_num) + ']/div//li')