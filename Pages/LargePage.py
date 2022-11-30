from selenium.webdriver.common.by import By


class LargePage:

    def __init__(self, browser):
        self.browser = browser

    # Variables
    URL = "https://the-internet.herokuapp.com/large"

    # Locators
    NESTED_DIVS = (By.XPATH, "//div[contains(@id,'sibling-')]")

    def visit(self):
        """
        Naviagtes to the given URL
        :return:
        """
        self.browser.get(self.URL)

    def nested_divs(self):
        """
        Returns the number of nested divs under "Siblings" header
        :return: integer
        """
        list_nested_divs = self.browser.find_elements(*self.NESTED_DIVS)
        number_nested_divs = len(list_nested_divs)

        return number_nested_divs
