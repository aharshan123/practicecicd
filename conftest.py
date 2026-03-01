from time import sleep

import pytest
from selenium.webdriver import Chrome,ChromeOptions,Firefox
o = ChromeOptions()
o.add_experimental_option("detach", True)

'''
@pytest.fixture(params=['chrome', 'firefox'])
def launch(request):
    if request.param == 'chrome':
        driver = Chrome(o)
    elif request.param == 'firefox':
        driver = Firefox()
    driver.quit()
'''

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def launch(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    yield driver
    driver.quit()

