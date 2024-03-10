from selenium.webdriver.support.ui import Select
from Utils.locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("http://omayo.blogspot.com")  # URL of the page

    def get_multi_selection_options(self):
        select = Select(self.browser.find_element(*HomePageLocators.MULTI_SELECTION_BOX))
        return [option.text for option in select.options]

    def get_hyperlink_href(self):
        try:
            # Wait for the hyperlink element to be present in the DOM
            hyperlink = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(HomePageLocators.HYPERLINK)
            )
            return hyperlink.get_attribute("href")
        except TimeoutException as e:
            print(f"{e}")
            # Handle the case where the element is not found within the timeout
            return None

    def get_multi_selection_box_header_text(self):
        header_element = self.browser.find_element(*HomePageLocators.MULTI_SELECTION_BOX_HEADER)
        return header_element.text

    def enter_search_text(self, text):
        search_input = self.browser.find_element(*HomePageLocators.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(text)

    def click_search_button(self):
        search_button = self.browser.find_element(*HomePageLocators.SEARCH_BUTTON)
        search_button.click()

    def is_search_executed(self):
        # This method needs to be defined based on how your application reacts to a search
        # For example, you might check if the URL has changed or if a certain element is now visible
        pass
    def trigger_alert_and_get_text(self):
        alert_button=self.browser.find_element(*HomePageLocators.ALERT_BUTTON)
        alert_button.click()
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())

        # Store the alert text in a variable
        alert_text = alert.text

        # Accept the alert (click "OK")
        alert.accept()

        return alert_text

    def accept_alert(self):
        try:
            # Wait for the alert to be present and then accept it
            alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert.accept()
            return True  # Return True to indicate success
        except TimeoutException:
            # If no alert is present within the timeout, return False
            return False
