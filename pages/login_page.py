from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Locators
        self.username_field = (By.XPATH, "//*[@name='username']")
        self.password_field = (By.XPATH, "//*[@name='password']")
        self.login_button = (By.XPATH, "//*[@type='submit']")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()