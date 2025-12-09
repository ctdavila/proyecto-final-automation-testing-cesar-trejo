def test_open_homepage(driver):
    """Verifica que la página cargue correctamente."""
    driver.get("https://talentolab-test.netlify.app/")
    assert "TL - Consultora" in driver.title


