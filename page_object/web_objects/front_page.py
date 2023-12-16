from selenium.webdriver.common.by import By

X_btn_first_popup = (By.XPATH, '//*[@class="affirm btn btn-primary btn-inline"]')
close_join_club = (By.XPATH, '(//*[@id="close-button"])[1]')


class Front_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_X_btn_first_popup(self):
        return self.driver.find_element(X_btn_first_popup[0], X_btn_first_popup[1])

    def get_strip_element_by_text(self, text):
        try:
            return self.driver.find_element(By.XPATH, '//h2[text()="' + text + '"]')
        except:
            raise AssertionError('Element Not Found')

    def get_close_join_club(self):
        return self.driver.find_element(close_join_club[0], close_join_club[1])

