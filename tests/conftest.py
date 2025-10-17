import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Inicia Chrome con Selenium Manager y cierra al final del test."""
    options = Options()
    options.add_argument("--start-maximized")
    # Si tu pantalla es chica: options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
