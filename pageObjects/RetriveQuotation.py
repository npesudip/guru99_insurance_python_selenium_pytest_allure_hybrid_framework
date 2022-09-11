from selenium.webdriver.common.by import By


class RetrieveQuotation:

    def __init__(self, driver):
        # self.title = None
        self.driver = driver

    retrieve_quotation_btn_id = "ui-id-3"
    identity_no_input_id = "id"
    retrieve_button_id = "getquote"

    def goto_retrieve_quotation_page(self):
        self.driver.find_element(By.ID, self.retrieve_quotation_btn_id).click()

    def set_quotation_number(self):
        self.driver.find_element(By.ID, self.identity_no_input_id).click()
        self.driver.find_element(By.ID, self.identity_no_input_id).send_keys(14080)

    def click_retrieve_submit(self):
        self.driver.find_element(By.ID, self.retrieve_button_id).click()
