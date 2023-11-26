from selenium import webdriver
import pytest
import os


Base_URL = "https://www.google.com/finance/"


@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Base_URL)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.split("::")[-1] + ".png"
        _capture_screenshot(os.path.join(os.getcwd(), 'screenshots', file_name))


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
