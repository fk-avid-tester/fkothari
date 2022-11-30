# Task Two

"""
This test verifies the number of nested divs under the "siblings" header
"""

from Pages.LargePage import LargePage


def test_nested_divs(browser):
    large_page = LargePage(browser)

    # Given we are on the large page
    large_page.visit()

    # Then number of nested divs under "siblings" header are 150
    assert large_page.nested_divs() == 150

