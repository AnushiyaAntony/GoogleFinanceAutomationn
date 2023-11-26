from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class Login(HomePage):

    def login_to_google_account(self, email, password):
        self.click_signin()
        username_element = self.driver.find_element(By.XPATH, "//input[@id='identifierId']")
        username_element.send_keys(email)
        next_button = self.driver.find_element(By.XPATH, "//button/span[text()='Next']")
        next_button.click()
        password_element = self.driver.find_element(By.XPATH, "//div[@id='password']//input")
        password_element.send_keys(password)
        next_button = self.driver.find_element(By.XPATH, "//button/span[text()='Next']")
        next_button.click()
