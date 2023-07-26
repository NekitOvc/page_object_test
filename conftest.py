from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import pytest

@pytest.fixture()
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture()
def browser(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()