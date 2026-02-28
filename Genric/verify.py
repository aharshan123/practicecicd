

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def verify_title(driver, expected_title):
    try:
        WebDriverWait(driver, 10).until(EC.title_is(expected_title))
    except:
        d = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        driver.save_screenshot(f"../screenshots/{d}.png")
        assert False, "Title mismatch"