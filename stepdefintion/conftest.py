import sys
import time

import pytest
from loguru import logger
from selenium import webdriver

def pytest_addoption(parser):
   parser.addoption("--browser")
   parser.addoption("--platform")
@pytest.fixture(autouse=True, scope="session")
def setup_and_teardown(request):

    logger.remove()
    logger.add(
        sys.stdout,
        format="{time:MM-DD-YYYY - hh:mm:ss} {level} --- <red>{message}</red>",
        level="INFO"
    )
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.get("https://www.hexschool.com/#")
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()


