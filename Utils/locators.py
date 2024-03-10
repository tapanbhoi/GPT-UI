from selenium.webdriver.common.by import By
#
# # Locators for HomePage elements
# class HomePageLocators:
#     # Assuming the multi-selection box can be uniquely identified by its header text
#     MULTI_SELECTION_BOX = (By.XPATH, "//h2[normalize-space()='Multi Selection box']/following-sibling::select[1]")
#     HYPERLINK = (By.XPATH, "//div[@class='tabs-outer']//p[1]")
#     # Add other locators here
# utils/locators.py

class HomePageLocators:
    MULTI_SELECTION_BOX = (By.XPATH, "//h2[normalize-space()='Multi Selection box']")
    MULTI_SELECTION_BOX_HEADER = (By.XPATH, "//h2[normalize-space()='Multi Selection box']")
    HYPERLINK = (By.XPATH, "//a[@id='selenium143']")
    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Search']")
    ALERT_BUTTON=(By.ID,"alert1")