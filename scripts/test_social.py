from time import sleep
import pytest

@pytest.mark.smoke
@pytest.mark.socialregression
@pytest.mark.regression
def test_facebook(launch):
    driver = launch
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    sleep(2)


@pytest.mark.socialregression
@pytest.mark.regression
def test_insta(launch):
    driver = launch
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    sleep(2)



