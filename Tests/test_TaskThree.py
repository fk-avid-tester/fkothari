"""
These tests are for challenging_dom page
"""

from Pages.ChallengingDomPage import ChallengingDomPage


def test_text_third_row(browser):
    """
    Test to verify the text value of the third row of the "Diceret column"
    :param browser:
    :return:
    """
    challenging_dom_page = ChallengingDomPage(browser)

    # Using chrome navigate directly to http://the-internet.herokuapp.com/challenging_dom
    challenging_dom_page.visit()

    col_num = challenging_dom_page.find_col_num_by_header_text("Diceret")

    text_third_row = challenging_dom_page.find_cell(col_num, 3).text

    assert text_third_row == "Phaedrum2"


def test_total_number_cells(browser):
    """
    Test to verify the total number of cells in the table, not including the header row
    :param browser:
    :return:
    """
    challenging_dom_page = ChallengingDomPage(browser)

    challenging_dom_page.visit()
    total_number_cells = challenging_dom_page.find_total_cells()
    assert total_number_cells == 70


def test_values_amet_column(browser):
    """
    Test to verify each value in the "Amet" column
    :param browser:
    :return:
    """
    challenging_dom_page = ChallengingDomPage(browser)

    challenging_dom_page.visit()

    challenging_dom_page.get_fifth_col_values()


def test_coordinates(browser):
    """
    Test to verify the co-ordinates of "Definiebas7" and "Iuvaret7"
    :param browser:
    :return:
    """
    challenging_dom_page = ChallengingDomPage(browser)

    challenging_dom_page.visit()

    col_coordinate_iuvaret7 = challenging_dom_page.find_col_num_by_header_text("Lorem")

    row_coordinate_iuvaret7 = challenging_dom_page.get_row_num_by_row_value_first_col("Iuvaret7")

    assert col_coordinate_iuvaret7 == 1
    assert row_coordinate_iuvaret7 == 8

    col_coordinate_definiebas7 = challenging_dom_page.find_col_num_by_header_text("Sit")

    row_coordinate_definiebas7 = challenging_dom_page.get_row_num_by_row_value_fourth_col("Definiebas7")

    assert col_coordinate_definiebas7 == 4
    assert row_coordinate_definiebas7 == 8


def test_click_green_button(browser):
    """
    Test to verify the values of on-screen buttons change after clicking the green button
    :param browser:
    :return:
    """
    challenging_dom_page = ChallengingDomPage(browser)

    challenging_dom_page.visit()

    before_click = challenging_dom_page.green_button_text()

    challenging_dom_page.click_green_button()

    after_click = challenging_dom_page.green_button_text()

    #   Assert that value of the green button before clicking is not the same as after clicking
    assert before_click != after_click
