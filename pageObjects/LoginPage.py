from selenium.webdriver.common.by import By


class LoginPage:
    login_box_xpath = "//input[@id='email']"
    password_box_xpath = "//input[@id='password']"
    login_btn_xpath = "//body/div[3]/form[1]/div[3]/input[1]"

    valid_username = "1guru99@getnada.com"
    valid_password = "Ts8uWFU2@eZb"
    username1 = ""
    password1 = ""

    def __init__(self, driver):
        # self.title = None
        self.driver = driver

    def set_email(self, username):
        self.driver.find_element(By.XPATH, self.login_box_xpath).click()
        self.driver.find_element(By.XPATH, self.login_box_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_box_xpath).click()
        self.driver.find_element(By.XPATH, self.password_box_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
