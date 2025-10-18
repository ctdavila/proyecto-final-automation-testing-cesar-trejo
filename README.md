# 🧪 Pre-Entrega QA Automatizado – Cesar Trejo

Este proyecto corresponde a la pre-entrega del curso de Testing QA Automatizado y tiene como objetivo aplicar los conocimientos adquiridos hasta la Clase 8.  
La práctica se realizó sobre el sitio [saucedemo.com](https://www.saucedemo.com/), una aplicación demo pensada para prácticas de testing automatizado.

---

## 📌 Propósito del Proyecto

El objetivo principal es **automatizar flujos básicos de navegación web** usando Selenium WebDriver con Python y gestionarlos bajo Pytest.  
De esta manera, se busca demostrar:

- La **capacidad para diseñar y estructurar casos de prueba automatizados**.  
- El uso de **esperas explícitas** (`WebDriverWait + Expected Conditions`) para aumentar la estabilidad de los tests.  
- El diseño de código **modular y organizado**, separando funciones auxiliares (helpers) en `utils/` y casos de prueba en `tests/`.  
- La integración con **Pytest-HTML** para la generación de reportes en HTML como evidencia de ejecución.

Los flujos automatizados incluyen:

1. **Login**  
   - Validar el inicio de sesión con credenciales válidas.  
   - Verificar redirección a `/inventory.html`.  
   - Comprobar título de la página ("Products") y título de la pestaña ("Swag Labs").  

2. **Catálogo de productos**  
   - Validar título correcto de la página de inventario.  
   - Verificar presencia de al menos un producto.  
   - Listar nombre y precio del primer producto visible.  
   - Confirmar la presencia de elementos clave de interfaz (menú, filtros).  

3. **Carrito de compras**  
   - Añadir un producto al carrito.  
   - Verificar incremento del contador del carrito (badge).  
   - Navegar al carrito y confirmar que el producto añadido aparece correctamente.  

---

## 🛠 Tecnologías Utilizadas

- **Lenguaje:** Python 3.9+  
- **Framework de pruebas:** Pytest  
- **Automatización:** Selenium WebDriver  
- **Reportes:** Pytest-HTML  
- **Control de versiones:** Git + GitHub  
- **Entorno virtual:** venv (para aislar dependencias)

---

## ⚙️ Instalación de Dependencias

Sigue estos pasos para instalar y preparar el proyecto en tu entorno local:

1. Clonar el repositorio:
   ```bash
   git clone git@github.com:ctdavila/pre-entrega-automation-testing-cesar-trejo.git
   cd pre-entrega-automation-testing-cesar-trejo
