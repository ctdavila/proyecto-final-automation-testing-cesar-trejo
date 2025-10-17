# utils/pages.py
"""
Funciones auxiliares para interactuar con saucedemo.com
Se usan en los tests para mantener el código organizado.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def login(driver, username, password, timeout=10):
    """Realiza login en Saucedemo con usuario/contraseña válidos."""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, timeout)

    user_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    pwd_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    user_input.clear()
    user_input.send_keys(username)
    pwd_input.clear()
    pwd_input.send_keys(password)
    login_btn.click()

def wait_inventory_page(driver, timeout=10):
    """Espera a que se cargue la página de inventario (/inventory.html)."""
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.url_contains("/inventory.html"))
    return wait

def get_inventory_title(driver, wait):
    """Devuelve el título visible en la página de inventario (esperado: 'Products')."""
    title_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    return title_el.text.strip()

def verify_tab_title_contains(driver, text="Swag Labs"):
    """Verifica que el título de la pestaña contenga un texto esperado (ej: 'Swag Labs')."""
    assert text in driver.title, f"Título de pestaña esperado '{text}', obtenido: '{driver.title}'"

def inventory_has_products(driver):
    """True si existe al menos un producto en el inventario."""
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    return len(items) > 0

def get_first_product_name_and_price(driver):
    """Devuelve (nombre, precio) del primer producto visible en el inventario."""
    name_el = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    price_el = driver.find_element(By.CLASS_NAME, "inventory_item_price")
    return name_el.text.strip(), price_el.text.strip()

def add_first_product_to_cart(driver, timeout=10):
    """Hace clic en 'Add to cart' del primer producto y retorna su nombre."""
    wait = WebDriverWait(driver, timeout)
    # Botón de agregar del primer producto
    add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button")))
    # Nombre del producto
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    add_button.click()
    return product_name

def go_to_cart(driver, timeout=10):
    """Hace clic en el ícono del carrito y espera a que cargue la página del carrito."""
    wait = WebDriverWait(driver, timeout)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    wait.until(EC.url_contains("/cart.html"))

