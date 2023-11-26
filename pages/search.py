import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class Search(HomePage):

    def search_and_return_text(self, stock):
        search_bar = self.driver.find_element(By.XPATH, "//div[@class='AyKEed']//input[@type='text' and @aria-label='Search for stocks, ETFs & more']")
        search_bar.send_keys("ITC  :NSE (IN)")
        time.sleep(2)
        options = self.driver.find_elements(By.XPATH, "//div[@role='listbox']/div/div/div[@jsslot]/div")
        stock_display_name = options[0].get_attribute('data-display-name')
        options[0].click()
        return stock_display_name
