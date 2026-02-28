from time import sleep

import pytest

@pytest.mark.smoke
@pytest.mark.ideregression
@pytest.mark.regression
def test_jetbrains(launch):
    driver = launch
    driver.get("https://www.jetbrains.com/")
    driver.maximize_window()
    sleep(2)

@pytest.mark.ideregression
@pytest.mark.regression
def test_eclipse(launch):
    driver = launch
    driver.get("https://www.eclipse.org/")
    driver.maximize_window()
    sleep(2)

def sample(launch):
    driver = launch
    driver.get("https://www.eclipse.org/")
    driver.maximize_window()
    sleep(2)

