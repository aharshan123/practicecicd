from time import sleep

import pytest
@pytest.mark.smoke
@pytest.mark.eduregression
@pytest.mark.regression
def test_udemy(launch):
    driver = launch
    driver.get("https://www.udemy.com/")
    driver.maximize_window()
    sleep(2)



@pytest.mark.eduregression
@pytest.mark.regression
def test_qsp(launch):
    driver = launch
    driver.get("https://qspiders.com/")
    driver.maximize_window()
    sleep(2)