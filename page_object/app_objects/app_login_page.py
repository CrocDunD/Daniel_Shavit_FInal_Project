from selenium.webdriver.common.by import By

login_btn = (By.XPATH,"//*[@id='login']")
login_with_email_btn = (By.XPATH, "//*[@text='Email']")
editable_field = (By.XPATH, "//*[@class='android.widget.EditText']")
continue_arrow = (By.XPATH, "//*[@class='android.widget.ImageView' and ./parent::*[@id='formFieldActionContainer']]")
sign_in_end_btn = (By.XPATH, "//*[@id='adidasStatefulInternalButton']")

class App_Login_Page:
    def __init__(self,driver):
        self.driver = driver

    def get_login_btn(self):
        return self.driver.find_element(login_btn[0],login_btn[1])

    def get_login_with_email_btn(self):
        return self.driver.find_element(login_with_email_btn[0],login_with_email_btn[1])

    def get_editable_field(self):
        return self.driver.find_element(editable_field[0], editable_field[1])

    def get_continue_arrow(self):
        return self.driver.find_element(continue_arrow[0],continue_arrow[1])

    def get_sing_in_end_btn(self):
        return self.driver.find_element(sign_in_end_btn[0],sign_in_end_btn[1])



