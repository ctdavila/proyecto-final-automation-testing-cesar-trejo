from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    # 1. Ir a la página de login
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # 2. Ingresar usuario y contraseña
    user_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    pwd_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    user_input.send_keys("standard_user")
    pwd_input.send_keys("secret_sauce")
    login_btn.click()

    # 3. Validar redirección a /inventory.html
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

    # 4. Validar texto "Products"
    title_el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    assert title_el.text.strip() == "Products", "El título visible no es 'Products'"

    # 5. Validar título de la pestaña
    assert "Swag Labs" in driver.title, "El título de la pestaña no contiene 'Swag Labs'"

