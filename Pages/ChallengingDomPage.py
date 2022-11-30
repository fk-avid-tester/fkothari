# Task 3

"""
This module contains ChallengingDomPage,
the page object for the Challenging DOM page on The Internet.
"""

from selenium.webdriver.common.by import By


class ChallengingDomPage:

    def __init__(self, browser):
        self.browser = browser

    # Variables
    URL = "http://the-internet.herokuapp.com/challenging_dom"

    # Locators
    START_BUTTON = (By.CSS_SELECTOR, "div[id='start'] button")
    TABLE_LOCATOR = (By.CSS_SELECTOR, "table")

    def visit(self):
        """
        Naviagtes to the given URL
        :return:
        """
        self.browser.get(self.URL)

    def find_table(self):
        """
        Returns locator for table element
        :return: locator
        """
        table = self.browser.find_element(*self.TABLE_LOCATOR)
        return table

    def find_col_num_by_header_text(self, text):
        """
        Returns column number for a given header text
        :param text:
        :return: integer
        """
        table = self.find_table()
        col_num = 1
        header_elements = table.find_elements(by=By.XPATH, value=".//th")
        for header_element in header_elements:
            if header_element.text == text:
                return col_num
            else:
                col_num += 1

    def find_cell(self, col_num, row_num):
        """
        Returns the xpath locator for a given row number and column number
        :param col_num:
        :param row_num:
        :return: xpath locator
        """
        table = self.find_table()
        return table.find_element(by=By.XPATH, value=".//tr[" + str(row_num) + "]/td[" + str(col_num) + "]")

    def find_total_cells(self):
        """
        Returns the total number of cells in the table, not including the Header row
        :return: integer
        """
        table = self.find_table()
        cells = table.find_elements(by=By.XPATH, value=".//tbody/tr/td")

        return len(cells)

    def get_fifth_col_values(self):
        """
        Prints all the values of the fifth column
        :return:
        """
        table = self.find_table()
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            row_values = row.find_elements(by=By.XPATH, value=".//td[5]")
            for value in row_values:
                print(value.text)

    def get_row_num_by_row_value_first_col(self, text):
        """
        Returns the row number for row value which matches given text in the first column
        :param text: row value
        :return: integer
        """
        table = self.find_table()
        row_num = 1
        row_elements = table.find_elements(by=By.XPATH, value=".//tr/td[1]")
        for row_element in row_elements:
            if row_element.text == text:
                print(row_num)
                return row_num
            else:
                row_num += 1

    def get_row_num_by_row_value_fourth_col(self, text):
        """
        Returns the row number for row vallue which matches given text in the fourth column
        :param text: row value
        :return: integer
        """
        table = self.find_table()
        row_num = 1
        row_elements = table.find_elements(by=By.XPATH, value=".//tr/td[4]")
        for row_element in row_elements:
            if row_element.text == text:
                return row_num
            else:
                row_num += 1

    def click_green_button(self):
        """
        Clicks the green button
        :return:
        """
        button = self.browser.find_element(by=By.CLASS_NAME, value='success')
        button.click()

    def green_button_text(self):
        """
        Returns the text value of green button
        :return: string
        """
        button = self.browser.find_element(by=By.CLASS_NAME, value='success')
        print(button.text)
        return button.text
