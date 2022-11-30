# Task One

"""
This test verifies the text returned after clicking start
"""

from Pages.DynamicLoadingPage import DynamicLoadingPage


def test_dynamic_loading(browser):
    dynamic_loading_page = DynamicLoadingPage(browser)

    # Given we are on the dynamic loading page
    dynamic_loading_page.visit()

    # When I click the Start button
    dynamic_loading_page.click_start()

    # Then I should see "Hello World!"
    finish_message = dynamic_loading_page.print_finish_message()
    assert finish_message == "Hello World!"
