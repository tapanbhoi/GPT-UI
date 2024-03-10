import pytest
from selenium import webdriver

# Pytest fixture to initialize and quit the driver
@pytest.fixture
def driver():
    # Setup code: runs before each test function
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Wait implicitly for elements to be ready.
    yield driver
    # Teardown code: runs after each test function
    driver.quit()

def test_open_new_tab(driver):
    # Open the initial page
    initial_url = "https://www.google.com"
    driver.get(initial_url)

    # Open a new tab with a specific URL
    new_tab_url = "https://www.python.org"
    driver.execute_script(f"window.open('{new_tab_url}');")

    # Open another new tab with a different URL
    second_new_tab_url = "https://www.selenium.dev"
    driver.execute_script(f"window.open('{second_new_tab_url}');")

    # Iterate over all open tabs
    all_opened_tabs = driver.window_handles
    all_titles = []
    for tab in all_opened_tabs:
        # Switch to the tab
        driver.switch_to.window(tab)
        # Get the title of the tab and print it
        title = driver.title
        all_titles.append(title)
        print(f"The title of the tab with handle {tab} is: {title}")

    # Example output:
    # The title of the tab with handle CDwindow-8DAB938DB65345C0F565631259684DEE is: Google
    # The title of the tab with handle CDwindow-A6BCA8810071AB92315272370FDE8933 is: Welcome to Python.org
    # The title of the tab with handle CDwindow-11E576868771BEB4D4417905F7F378CC is: Selenium

    # Assert to ensure all tabs have the correct titles
    assert "Google" in all_titles, "Google tab is not open"
    assert "Welcome to Python.org" in all_titles, "Python.org tab is not open"
    assert "Selenium" in all_titles, "Selenium.dev tab is not open"

    # Switch back to the original tab if necessary
    driver.switch_to.window(driver.window_handles[0])

# The rest of your pytest code...
