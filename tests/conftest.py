import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()))
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

