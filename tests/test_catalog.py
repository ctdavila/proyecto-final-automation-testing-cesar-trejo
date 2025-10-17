from utils.pages import (
    login,
    wait_inventory_page,
    get_inventory_title,
    verify_tab_title_contains,
    inventory_has_products,
    get_first_product_name_and_price,
)
from selenium.webdriver.common.by import By

def test_catalog_elements_and_first_item(driver):
    """
    Caso de Navegación y Verificación del Catálogo:

    Criterios mínimos:
    - Valida título 'Products'
    - Valida presencia de productos
    - Lista nombre/precio del primero
    Además: valida UI clave (menú y filtros)
    """
    # 1) Login y navegación al inventario
    login(driver, "standard_user", "secret_sauce")
    wait = wait_inventory_page(driver)  # espera explícita de URL /inventory.html

    # 2) Validar título 'Products' y título de pestaña 'Swag Labs'
    assert get_inventory_title(driver, wait) == "Products", "El título de inventario no es 'Products'."
    verify_tab_title_contains(driver, "Swag Labs")

    # 3) Validar que haya productos visibles
    assert inventory_has_products(driver), "No se encontraron productos en el inventario."

    # 4) Obtener y listar nombre + precio del primer producto
    name, price = get_first_product_name_and_price(driver)
    # Asserts básicos para garantizar datos correctos
    assert name != "", "El nombre del primer producto está vacío."
    assert price.startswith("$"), f"Precio inválido en el primer producto: {price}"

    # 5) Validar elementos importantes de la UI (menú y filtros)
    # Menú hamburguesa
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_btn.is_displayed(), "El botón de menú no está visible."

    # Selector de ordenamiento (filtros)
    sort_select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert sort_select.is_displayed(), "El control de filtros no está visible."

    # (Opcional) Log de consola para el reporte
    print(f"[INFO] Primer producto -> Nombre: {name} | Precio: {price}")
