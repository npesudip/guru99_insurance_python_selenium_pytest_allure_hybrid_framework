import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilHelper.string_generator import get_random_string


class LandingPage:
    def __init__(self, driver):
        # self.title = None
        self.driver = driver

    request_quotation_link_text = "Request Quotation"

    break_down_cover_dropdown_xpath = "//select[@id='quotation_breakdowncover']"
    breakdown_options = ["No cover", "Roadside", "At home", "European"]

    wind_screen_repair_radio_yes_xpath = "//label[contains(text(),'YES')]"
    wind_screen_repair_radio_no_xpath = "//label[contains(text(),'NO')]"

    wind_screen_repair_choice = [wind_screen_repair_radio_yes_xpath, wind_screen_repair_radio_no_xpath]
    wind_screen_repair_choice = random.choice(wind_screen_repair_choice)

    incidents_box_xpath = "//input[@id='quotation_incidents']"
    registration_box_xpath = "//input[@id='quotation_vehicle_attributes_registration']"
    annual_mileage_box_xpath = "//input[@id='quotation_vehicle_attributes_mileage']"
    estimated_value_box_xpath = "//input[@id='quotation_vehicle_attributes_value']"
    parking_location_dropdown_xpath = "//select[@id='quotation_vehicle_attributes_parkinglocation']"

    start_of_policy_dropdown_year_id = "quotation_vehicle_attributes_policystart_1i"
    start_of_policy_dropdown_month_id = "quotation_vehicle_attributes_policystart_2i"
    start_of_policy_dropdown_day_id = "quotation_vehicle_attributes_policystart_3i"

    save_quotation_button_name = "submit"

    quotation_number_text_xpath = "//b[normalize-space()='Your identification number is :']"

    def goto_request_quotation(self):
        self.driver.find_element(By.LINK_TEXT, self.request_quotation_link_text).click()

    def goto_break_down_cover(self):
        select = Select(self.driver.find_element(By.XPATH, self.break_down_cover_dropdown_xpath).click())
        select.select_by_visible_text(random.choice(self.breakdown_options)).click()

    def goto_wind_screen_repair(self):
        self.driver.find_element(By.XPATH, self.wind_screen_repair_choice).click()

    def set_incidents(self):
        self.driver.find_element(By.XPATH, self.incidents_box_xpath).click()
        self.driver.find_element(By.XPATH, self.incidents_box_xpath).send_keys(get_random_string(8))

    def set_registration(self):
        self.driver.find_element(By.XPATH, self.registration_box_xpath).click()
        self.driver.find_element(By.XPATH, self.registration_box_xpath).send_keys(get_random_string(8))

    def set_annual_millage(self):
        self.driver.find_element(By.XPATH, self.annual_mileage_box_xpath).click()
        self.driver.find_element(By.XPATH, self.annual_mileage_box_xpath).send_keys(get_random_string(8)
                                                                                    )

    def set_estimated_value(self):
        self.driver.find_element(By.XPATH, self.estimated_value_box_xpath).click()
        self.driver.find_element(By.XPATH, self.estimated_value_box_xpath).send_keys(get_random_string(8)
                                                                                     )

    def set_parking_location(self):
        select = Select(self.driver.find_element(By.XPATH, self.parking_location_dropdown_xpath).click())
        select.select_by_index(random.randint(0, 6)).click()

    def set_date(self):
        select = Select(self.driver.find_element(By.ID, self.start_of_policy_dropdown_year_id).click())
        select.select_by_index(random.randint(0, 11)).click()

        select = Select(self.driver.find_element(By.ID, self.start_of_policy_dropdown_month_id).click())
        select.select_by_index(random.randint(0, 11)).click()

        select = Select(self.driver.find_element(By.ID, self.start_of_policy_dropdown_day_id).click())
        select.select_by_index(random.randint(0, 31)).click()

    def click_submit(self):
        self.driver.find_element(By.NAME, self.save_quotation_button_name).click()

    def get_quotation_number(self):
        quotation_number_text = self.driver.find_element(By.XPATH, self.quotation_number_text_xpath).click()
        action = ActionChains(self.driver)
        quotation_number_text = action.double_click(quotation_number_text)
        quotation_number = [int(s) for s in quotation_number_text.split() if s.isdigit()]
        return quotation_number
