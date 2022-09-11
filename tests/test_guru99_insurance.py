import os
import sys
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from utilHelper.email_generator import *

from pageObjects.PageActionMethods import PageMethods
from utilHelper.customLogger import LogGen
from utilHelper.readProperties import ReadConfig

os.chdir(os.path.dirname(sys.argv[0]))

config_obj = ReadConfig
page_url = config_obj.getApplicationURL()
print(page_url)


@allure.severity(allure.severity_level.NORMAL)
class Test_Insurance:
    logger = LogGen.loggen()  # Logger

    @allure.severity(allure.severity_level.MINOR)
    def test_home_page_title(self, setup):
        actual_title = "Insurance Broker System - Login"
        self.driver = setup
        self.driver.get(page_url)
        home_page_title = self.driver.title
        self.driver.save_screenshot("..//Screenshots//" + "login_test.png")

        if home_page_title == actual_title:
            assert True
            self.driver.close()

        else:
            allure.attach(self.driver.save_screenshot_as_png, name="test_home_page_title",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_page_positive_testing(self, setup):
        actual_title = "Insurance Broker System"
        self.logger.info("************* test_login_page **********")
        self.driver = setup
        self.driver.get(page_url)
        self.driver.maximize_window()
        self.guru_driver = PageMethods(self.driver)
        self.guru_driver.set_email()
        time.sleep(0.5)
        self.guru_driver.set_password()
        time.sleep(0.5)
        self.guru_driver.click_login_button()
        title = self.driver.title
        print(title)

        if title == actual_title:
            assert True
            self.driver.close()

        else:
            allure.attach(self.driver.save_screenshot_as_png, name="test_login_page",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_page_negative_testing(self, setup):
        actual_title = "Insurance Broker System"
        self.logger.info("************* test_login_page **********")
        self.driver = setup
        self.driver.get(page_url)
        self.driver.maximize_window()
        self.guru_driver = PageMethods(self.driver)
        self.guru_driver.set_email(email_generator())
        time.sleep(0.5)
        self.guru_driver.set_password()
        time.sleep(0.5)
        self.guru_driver.click_login_button()
        title = self.driver.title
        print(title)

        if title == actual_title:
            assert True
            self.driver.close()

        else:
            allure.attach(self.driver.save_screenshot_as_png, name="test_login_page",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_request_quotation(self, setup):
        actual_title = "Insurance Broker System"
        self.logger.info("************* test_request_quotation **********")
        self.driver = setup
        self.driver.get(page_url)
        self.driver.maximize_window()
        self.guru_driver = PageMethods(self.driver)
        self.guru_driver.login_method()

        self.guru_driver.goto_request_quotation()
        time.sleep(0.5)
        self.guru_driver.set_break_down_cover()
        time.sleep(0.5)

        self.guru_driver.set_wind_screen_repair()
        time.sleep(0.5)

        self.guru_driver.set_incidents()
        time.sleep(0.5)

        self.guru_driver.set_registration()
        time.sleep(0.5)

        self.guru_driver.set_annual_millage()
        time.sleep(0.5)

        self.guru_driver.set_estimated_value()
        time.sleep(0.5)

        self.guru_driver.set_parking_location()
        time.sleep(0.5)

        self.guru_driver.set_date()
        time.sleep(0.5)

        self.guru_driver.click_submit()
        time.sleep(0.5)

        quotation_number = self.guru_driver.get_quotation_number()
        print(quotation_number)

        if quotation_number == actual_title:
            assert True
            self.driver.close()

        else:

            allure.attach(self.driver.save_screenshot_as_png, name="test_login_page",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_quotation(self, setup):
        actual_title = "Insurance Broker System"

        quotation_number = [14079, 14078, 14080, 14081]  # testdata for this testcase
        self.logger.info("************* test_get_quotation **********")
        self.driver = setup
        self.driver.get(page_url)
        self.driver.maximize_window()
        self.guru_driver = PageMethods(self.driver)
        self.guru_driver.login_method()

        self.guru_driver.goto_retrieve_quotation_page()
        time.sleep(0.5)

        self.guru_driver.set_quotation_number()
        time.sleep(0.5)

        self.guru_driver.click_retrieve_submit()
        quotation_page_title = self.driver.title

        if quotation_page_title == actual_title:
            assert True
            self.driver.close()

        else:

            allure.attach(self.driver.save_screenshot_as_png, name="test_login_page",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, setup):
        page_title_after_logout = "Insurance Broker System - Login"
        self.driver = setup
        self.driver.get(page_url)
        self.driver.maximize_window()
        self.guru_driver = PageMethods(self.driver)
        self.guru_driver.login_method()
        self.driver.logout()
        actual_title = self.driver.title

        if page_title_after_logout == actual_title:
            assert True
            self.driver.close()

        else:
            allure.attach(self.driver.save_screenshot_as_png, name="test_login_page",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
