from utils.pages import (
    login,
    add_first_product_to_cart,
    go_to_cart,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart(driver):
    """
    Interacción con Productos (Carrito) - Clase 8

    Pasos:
    1) Login con usuario válido
    2) Agregar PRIMER producto al carrito
    3) Validar que el contador del carrito sea '1'
    4) Abrir el carrito
    5) Validar que el producto agregado esté en la lista del carrito

    Criterios mínimos:
    - Agrega primer producto
    - Verifica ítem en carrito
    """

    # 1) Login
    login(driver, "standard_user", "secret_sauce")

    # 2) Agregar primer producto y guardar su nombre
    product_name = add_first_product_to_cart(driver)

    # 3) Validar el badge del carrito = 1
    wait = WebDriverWait(driver, 10)
    cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1", f"El contador del carrito no es 1 (fue {cart_badge.text})"

    # 4) Abrir el carrito
    go_to_cart(driver)

    # 5) Validar que el PRIMER ítem del carrito coincide con el agregado
    cart_item_name = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    assert cart_item_name.text.strip() == product_name, (
        f"El producto en el carrito ('{cart_item_name.text}') no coincide con el agregado ('{product_name}')."
    )
