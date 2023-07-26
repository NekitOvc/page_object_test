import time
from google_page import SearchHelper
from selenium.webdriver.common.by import By

def test_google_search(browser):
    google_page = SearchHelper(browser)
    google_page.go_to_site()
    google_page.enter_word('Page Object')
    time.sleep(2)
    google_page.click_on_the_search_button()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="logo"]/img')