import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Read test data from JSON file
def read_test_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Test fixture to initialize WebDriver
@pytest.fixture(scope='module')
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Test function to validate login with different username and password combinations
def test_login_with_multiple_input_parameters(setup):
    # Initialize WebDriver
    driver = setup

    # Read test data from JSON file
    test_data = read_test_data_from_json('test_data.json')

    # Navigate to the login page
    driver.get("https://stackoverflow.com/users/login")

    # Loop through each set of test data
    for data in test_data:
        # Enter username and password from test data
        username_input = driver.find_element(By.ID, "email")
        username_input.clear()
        username_input.send_keys(data['username'])

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(data['password'])

        # Click on the login button
        login_button = driver.find_element(By.XPATH, "//button[@id='submit-button']")
        login_button.click()

        # Check if login is successful or not based on expected outcome from test data
        if data['expected_success']:
            # Assert that the user is redirected to the profile page after successful login
            assert "/users/" in driver.current_url, f"Expected to be redirected to user profile page after successful login, Actual URL: {driver.current_url}"
        else:
            # Assert that the login fails and the user remains on the login page
            assert "/users/login" in driver.current_url, f"Expected login to fail and remain on the login page, Actual URL: {driver.current_url}"
