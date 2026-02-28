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

import pytest

passed = 0
failed = 0

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global passed, failed
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            passed += 1
        elif report.failed:
            failed += 1

@pytest.fixture(scope="session", autouse=True)
def final_count():
    yield
    print("\n======================")
    print("Passed Testcases :", passed)
    print("Failed Testcases :", failed)
    print("======================")

