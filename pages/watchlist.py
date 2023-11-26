from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from pages.home_page import HomePage


class Watchlist(HomePage):

    def click_create_watchlist(self):
        self.launch_main_menu()
        add_w = self.driver.find_element(By.XPATH, "//button[@aria-label='Create watchlist']")
        add_w.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='headingText']")))
        return self.driver.find_element(By.XPATH, "//*[@id='headingText']/span").text

    def create_watchlist(self, w):
        self.launch_main_menu()
        add_w = self.driver.find_element(By.XPATH, "//button[@aria-label='Create watchlist']")
        add_w.click()
        dialog = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='VfPpkd-P5QLlc' and @role='dialog']")))
        name = dialog.find_element(By.XPATH, "//input[@type='text']")
        name.send_keys(w)
        save = self.driver.find_element(By.XPATH, "//button/span[text()='Save']")
        save.click()

    def launch_watchlist(self,w):
        self.launch_main_menu()
        portfolio = self.driver.find_element(By.XPATH, f"//a[@role='menuitem' and @title='{w}']")
        portfolio.click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@role='heading' and text()='{w}']")))

    def add_single_investment(self, investment):
        add_inv = self.driver.find_element(By.XPATH, "//button/span[text()='Add investments']")
        add_inv.click()
        dialog = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='Type an investment name or symbol']")))
        dialog.send_keys(investment)
        options = self.driver.find_elements(By.XPATH, "//div[@role='listbox']/div/div/div[@jsslot]/div")
        options[0].click()
        save = self.driver.find_element(By.XPATH, "//button/span[text()='Save']")
        save.click()
