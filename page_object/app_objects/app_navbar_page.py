from selenium.webdriver.common.by import By


item_bag_total = (By.XPATH, "//*[@id='menuItemBadge']")
profile_btn = (By.XPATH, "//*[@id='profileButton']")
navbar_btn = (By.XPATH, "(//*[@id='navigation_bar_item_icon_view'])["+"]")


class App_Navbar_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_navbar_btn(self, number):
        return self.driver.find_element(By.XPATH, "(//*[@id='navigation_bar_item_icon_view'])[" + str(number) + "]")


    def get_item_bag_total(self):
        return self.driver.find_element(item_bag_total[0],item_bag_total[1])

    def get_profile_btn(self):
        return self.driver.find_element(profile_btn[0],profile_btn[1])
