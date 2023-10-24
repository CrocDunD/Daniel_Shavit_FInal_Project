from selenium.webdriver.common.by import By


item_bag_total = (By.XPATH, "//*[@id='menuItemBadge']")


class App_Navbar_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_navbar_button(self):
        self.driver.find_element(By.XPATH, "(//*[@id='navigation_bar_item_icon_view'])[2]")

    def get_item_bag_total(self):
        return self.driver.find_element(item_bag_total[0],item_bag_total[1])


