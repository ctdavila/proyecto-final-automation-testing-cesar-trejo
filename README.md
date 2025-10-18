# Pre-Entrega QA Automatizado – Cesar Trejo

Automatización de flujos básicos en [saucedemo.com](https://www.saucedemo.com/) con **Python + Selenium + Pytest**.

##  Propósito
Validar:
- **Login** exitoso (redirección a `/inventory.html`, título "Products", pestaña "Swag Labs").
- **Catálogo** (título correcto, productos visibles, nombre y precio del primero, menú y filtros presentes).
- **Carrito** (agregar primer producto, validar badge "1", verificación del ítem en el carrito).

##  Tecnologías
- Python 3
- Selenium WebDriver
- Pytest
- Pytest-HTML

##  Instalación de Dependencias

1. Clonar el repositorio:
   ```bash
   git clone git@github.com:ctdavila/pre-entrega-automation-testing-cesar-trejo.git
   cd pre-entrega-automation-testing-cesar-trejo
