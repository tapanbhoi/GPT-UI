from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://stackoverflow.com/users/login?ssrc=head"  # Replace with your login page URL
        self.username_input = (By.XPATH, "//a[normalize-space()='Log in']']")  # Replace with the actual locator
        self.password_input = (By.XPATH, "//input[@class='flex--item s-input']")  # Replace with the actual locator
        self.login_button = (By.XPATH, "//button[@id='submit-button']")  # Replace with the actual locator

    def load(self):
        self.browser.get(self.url)

    def login(self, username, password):
        self.browser.find_element(*self.username_input).send_keys(username)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()
