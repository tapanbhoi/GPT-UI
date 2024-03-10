import pytest
import json
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from Pages.login_page import LoginPage
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Load test data
with open("Test-Data/login_data.json") as file:
    test_data = json.load(file)

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(browser):
    logger.info("Starting test_valid_login")
    login_page = LoginPage(browser)
    login_page.load()
    valid_data = test_data["valid_credentials"]
    login_page.login(valid_data["username"], valid_data["password"])
    assert "dashboard" in browser.current_url, "Login failed for valid credentials"

def test_blank_username(browser):
    logger.info("Starting test_blank_username")
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("", "somepassword")  # Blank username
    error_message = browser.find_element_by_id("error").text  # Assuming error message has an ID 'error'
    assert "Username required" in error_message, "No error for blank username"

def test_blank_password(browser):
    logger.info("Starting test_blank_password")
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("someuser", "")  # Blank password
    error_message = browser.find_element_by_id("error").text
    assert "Password required" in error_message, "No error for blank password"

def test_incorrect_password(browser):
    logger.info("Starting test_incorrect_password")
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("validuser", "wrongpassword")
    error_message = browser.find_element_by_id("error").text
    assert "Invalid credentials" in error_message, "No error for incorrect password"

def test_login_page_elements(browser):
    logger.info("Starting test_login_page_elements")
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.is_element_present("username_input"), "Username input not present"
    assert login_page.is_element_present("password_input"), "Password input not present"
    assert login_page.is_element_present("login_button"), "Login button not present"
