import pytest
from Pages.home_page import HomePage
@pytest.fixture(scope="module")
def home_page(browser):
    home_page = HomePage(browser)
    home_page.load()
    return home_page
# def test_multi_selection_box_options(browser):
#     home_page = HomePage(browser)
#     home_page.load()
#
#     options = home_page.get_multi_selection_options()
#     expected_options = ["Volvo", "Swift", "Hyundai", "Audi"]
#     assert set(options) == set(expected_options), "Multi-selection box options do not match expected values"

def test_hyperlink_href(browser):
    home_page = HomePage(browser)
    home_page.load()


    expected_href = "http://www.selenium143.blogspot.com/".lower()
    actual_href = home_page.get_hyperlink_href()

    assert actual_href is not None, "Hyperlink could not be found."
#    assert actual_href.lower() == expected_href, "Hyperlink HREF does not match expected value"
def test_multi_selection_box_header_text(browser):
    home_page = HomePage(browser)
    home_page.load()

    header_text = home_page.get_multi_selection_box_header_text()
    expected_text = "Multi Selection box"
    assert header_text == expected_text, f"Header text does not match. Expected: '{expected_text}', Got: '{header_text}'"

def test_search_functionality(browser):
    home_page = HomePage(browser)
    home_page.load()

    search_query = "test"  # Replace with a valid search term for your application
    home_page.enter_search_text(search_query)
    home_page.click_search_button()

    # Replace the following assert with an appropriate condition for your application
    # For example, if a new page is loaded or if search results become visible
    assert home_page.is_search_executed(), "Search was not executed properly"
def test_alert(browser):
    home_page=HomePage(browser)
    home_page.load()
    alert_text=home_page.trigger_alert_and_get_text()
    Expected_text="Hello"
    assert alert_text==Expected_text,"Elert not generating"

