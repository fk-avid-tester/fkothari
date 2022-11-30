"""
This module contains DynamicLoadingPage,
the page object for the Dynamic Loading page on The Internet.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DynamicLoadingPage:

    def __init__(self, browser):
        self.browser = browser

    # Variables
    URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

    # Locators
    START_BUTTON = (By.CSS_SELECTOR, "div[id='start'] button")
    FINISH_MESSAGE = (By.CSS_SELECTOR, "div[id='finish'] h4")

    def visit(self):
        """
        Naviagtes to the given URL
        :return:
        """
        self.browser.get(self.URL)

    def click_start(self):
        """
        Clicks start button
        :return:
        """
        start_button = self.browser.find_element(*self.START_BUTTON)
        start_button.click()

    def print_finish_message(self):
        """
        Returns finish message when the page has finished loading after clicking start
        :return:
        """
        # wait for the load to finish above
        try:
            finish_message = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "finish"))
            )

            return finish_message.text
        except TimeoutException:
            print('Timed out waiting for Finished Message to be visible')
            raise
