import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.PageElementsCollections import PageElements

from pageObjects.PageElementsCollections import PageElements as pe
from utilHelper.string_generator import get_random_string


class Logout:
    def __init__(self, driver):
        # self.title = None
        self.driver = driver

    # element locators
    logout_button_xpath = "//input[@value='Log out']"

    def logout(self):
        self.driver.find_element(By.ID, self.logout_button_xpath).click()
