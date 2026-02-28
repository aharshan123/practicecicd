from time import sleep
import pytest
from Genric.verify import *

@pytest.mark.smoke
@pytest.mark.ecomregression
@pytest.mark.regression
def test_myntra(launch):
    driver = launch
    driver.get("https://www.myntra.com/")
    driver.maximize_window()
    verify_title(driver, "Online Shopping fr Women, Men, Kids Fashion & Lifestyle - Myntra")
    sleep(2)


@pytest.mark.ecomregression
@pytest.mark.regression
def test_flipkart(launch):
    driver = launch
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    sleep(2)