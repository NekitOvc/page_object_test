from base_app import BasePage
from selenium.webdriver.common.by import By

class Locators:
    SEARCH_BAR = (By.CLASS_NAME, 'gLFyf')
    SEARCH_BUTTON = (By.CLASS_NAME, 'gNO89b')

class SearchHelper(BasePage):
    def enter_word(self, word):
        search_bar = self.find_element(Locators.SEARCH_BAR)
        search_bar.click()
        search_bar.send_keys(word)
        return search_bar

    def click_on_the_search_button(self):
        return self.find_element(Locators.SEARCH_BUTTON).click()