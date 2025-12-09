import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"

            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            filepath = os.path.join(screenshots_dir, filename)

            driver.save_screenshot(filepath)

            print(f"\nScreenshot guardado en: {filepath}")

