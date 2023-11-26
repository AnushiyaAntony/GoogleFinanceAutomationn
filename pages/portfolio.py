from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class Portfolio(HomePage):

    def click_create_portfolio(self):
        self.launch_main_menu()
        add_p = self.driver.find_element(By.XPATH, "//button[@aria-label='Create portfolio']")
        add_p.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='headingText']")))
        return self.driver.find_element(By.XPATH, "//*[@id='headingText']/span").text

    def create_portfolio(self, p):
        self.launch_main_menu()
        add_p = self.driver.find_element(By.XPATH, "//button[@aria-label='Create portfolio']")
        add_p.click()
        dialog = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='VfPpkd-P5QLlc' and @role='dialog']")))
        name = dialog.find_element(By.XPATH, "//input[@type='text']")
        name.send_keys(p)
        save = self.driver.find_element(By.XPATH, "//button/span[text()='Save']")
        save.click()

    def launch_portfolio(self,p):
        self.launch_main_menu()
        portfolio = self.driver.find_element(By.XPATH, f"//a[@role='menuitem' and @title='{p}']")
        portfolio.click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@role='heading' and text()='{p}']")))

    def add_single_investment(self, investment):
        add_inv = self.driver.find_element(By.XPATH, "//button/span[text()='Add investments']")
        add_inv.click()
        dialog = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='VfPpkd-P5QLlc' and @role='dialog']")))
        name = dialog.find_element(By.XPATH, "//input[@type='text']")
        name.send_keys(investment)
        options = self.driver.find_elements(By.XPATH, "//div[@role='listbox']/div/div/div[@jsslot]/div")
        options[0].click()
        save = self.driver.find_element(By.XPATH, "//button/span[text()='Save']")
        save.click()

    def add_multiple_investments(self, investments):
        add_inv = self.driver.find_element(By.XPATH, "//button/span[text()='Add investments']")
        add_inv.click()
        dialog = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='VfPpkd-P5QLlc' and @role='dialog']")))
        name = dialog.find_element(By.XPATH, "//input[@type='text']")
        for i in investments:
            name.clear()
            name.send_keys(i)
            options = self.driver.find_elements(By.XPATH, "//div[@role='listbox']/div/div/div[@jsslot]/div")
            options[0].click()
            save_and_add = self.driver.find_element(By.XPATH, "//button/span[text()='Save & add another']")
            save_and_add.click()
        cancel = self.driver.find_element(By.XPATH, "//button/span[text()='Cancel']")
        cancel.click()

    def get_investments_in_a_portfolio(self, p):
        self.launch_portfolio(p)
        inv = (self.driver.find_element
               (By.XPATH, "//div[@role='complementary]//div[@jsslot]/span[text()='p']/following-sibling::div"))
        return inv.text
