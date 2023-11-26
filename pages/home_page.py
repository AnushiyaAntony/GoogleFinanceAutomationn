from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_signin(self):
        signin = (self.driver.find_element
                  (By.XPATH, "//a[contains(@href,'https://accounts.google.com/ServiceLogin')]/span[text()='Sign in']"))
        signin.click()

    def main_page_visible(self):
        return self.wait.until(EC.title_contains('Google Finance'))

    def get_page_title(self):
        return self.driver.title

    def launch_main_menu(self):
        menu = self.driver.find_element(By.XPATH,"//header[@id='gb']//div[@aria-label='Main menu']")
        menu.click()
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-is-loaded='true']")))

    def follow_stock(self):
        follow = self.wait.until(EC.visibility_of_element_located
                                 ((By.XPATH, "//div[@class='U7usId']/div[text()='Follow']")))
        follow.click()
        return self.driver.find_element(By.XPATH, "//*[@id='headingText']/span").text

    def launch_market_trends(self):
        self.launch_main_menu()
        mkt = self.driver.find_element(By.XPATH, "//a[@title='Market trends']")
        mkt.click()
        markets = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='TnyjJd']")))
        return markets.text

    def verify_earnings_calendar(self):
        return self.wait.until(EC.visibility_of_element_located
                               ((By.XPATH,"//div[@role='heading' and @id='events-heading']"))).text

    def verify_market_trends_in_home_page(self):
        return self.wait.until(EC.visibility_of_element_located
                               ((By.XPATH, "//div[@role='heading' and @id='todays-tickers-heading']"))).text

    def verify_most_followed_in_home_page(self):
        return self.wait.until(EC.visibility_of_element_located
                               ((By.XPATH, "//div[@role='heading' and @id='most-folowed-header']"))).text

    def verify_in_news_in_markets_explorer(self):
        self.launch_main_menu()
        mkt = self.driver.find_element(By.XPATH, "//a[@title='Market trends']")
        mkt.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='TnyjJd']")))
        return self.wait.until(EC.visibility_of_element_located
                               ((By.XPATH, "//div[@role='heading' and @id='it3LM']"))).text
