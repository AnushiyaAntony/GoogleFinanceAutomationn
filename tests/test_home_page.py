from pages.home_page import HomePage
from pages.search import Search
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from pages.portfolio import Portfolio
from pages.watchlist import Watchlist
import pytest


@pytest.mark.smoke
def test_page_title(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.get_page_title() == "Google Finance - Stock Market Prices, Real-time Quotes & Business News",\
        "Page title is not as expected"


def test_search_function(setup_teardown):
    driver = setup_teardown
    search_obj = Search(driver)
    assert search_obj.main_page_visible()
    stock_name = search_obj.search_and_return_text("ITC")
    result = search_obj.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='heading' and @class='zzDege']")))
    assert result.text == stock_name, "Searched stock not present in home page"


@pytest.mark.smoke
def test_follow_stock(setup_teardown):
    driver = setup_teardown
    search_obj = Search(driver)
    home_obj = HomePage(driver)
    assert search_obj.main_page_visible()
    search_obj.search_and_return_text("ITC")
    choose_or_signin_account = home_obj.follow_stock()
    assert choose_or_signin_account == 'Choose an account' or 'Sign in', "No option shown to login to google account"


@pytest.mark.smoke
def test_launch_main_menu(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.launch_main_menu(), "Main Menu not launched"


def test_create_portfolio(setup_teardown):
    driver = setup_teardown
    portfolio=Portfolio(driver)
    choose_or_signin_account = portfolio.click_create_portfolio()
    assert choose_or_signin_account == 'Choose an account' or 'Sign in', "No option shown to login to google account"


def test_create_watchlist(setup_teardown):
    driver = setup_teardown
    watchlist_obj = Watchlist(driver)
    choose_or_signin_account = watchlist_obj.click_create_watchlist()
    assert choose_or_signin_account == 'Choose an account' or 'Sign in', "No option shown to login to google account"


def test_launch_market_trends(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.main_page_visible()
    assert 'Explore market trends' in home_obj.launch_market_trends(), "Market Trends not launched"


@pytest.mark.smoke
def test_earnings_calendar(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.main_page_visible()
    assert home_obj.verify_earnings_calendar() == 'Earnings calendar', "Earnings calendar not present in home page"


@pytest.mark.smoke
def test_verify_market_trends_in_home_page(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.main_page_visible()
    assert home_obj.verify_market_trends_in_home_page() == 'Market trends', "Market trends not present in home page"


@pytest.mark.smoke
def test_verify_most_followed_in_home_page(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.main_page_visible()
    assert home_obj.verify_most_followed_in_home_page() == 'Most followed on Google', "Most followed on Google not present in home page"


@pytest.mark.smoke
def test_verify_in_news_in_markets_explorer(setup_teardown):
    driver = setup_teardown
    home_obj = HomePage(driver)
    assert home_obj.main_page_visible()
    assert home_obj.verify_in_news_in_markets_explorer() == 'In the news', "In the news not present in markets explorer"