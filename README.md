# Proyecto de Talento Tech

## Propósito del proyecto
Este proyecto nace con la idea de practicar y consolidar habilidades de automatización, aplicando pruebas de UI y API sobre el sitio SauceDemo. La intención no es solo automatizar, sino también construir una base sólida con buenas prácticas como Page Object Model, manejo de datos externos, generación automática de reportes, logs claros y evidencias visuales para cada prueba fallida.

## Tecnologías utilizadas
- Python 3.x
- Pytest
- Selenium WebDriver
- Logging
- Faker
- CSV / JSON
- Requests

### Reportes y Logs
Durante la ejecución, el proyecto genera diferentes tipos de resultados que ayudan tanto al análisis técnico como al seguimiento del proceso: reporte HTML, capturas de pantalla y archivo de logs.

## Reporte HTML
Al finalizar la ejecución, se crea un archivo reporte.html en la carpeta raíz, donde se puede ver el detalle de cada caso de prueba: su estado, duración y cualquier evidencia disponible.

## Logs de ejecución
Se registra toda la actividad de las pruebas en el archivo:
logs/suite.log
Este archivo permite entender qué ocurrió internamente durante la ejecución, facilitando el análisis y la trazabilidad.


## Capturas de pantalla
Cuando una prueba falla, se guarda automáticamente una captura en:
reports/screens/
Estas evidencias visuales ayudan a identificar rápidamente qué salió mal.

## Ejecutar todas las pruebas
Para ejecutar toda la suite de pruebas, simplemente corré:
python -m run_test.py

## ¿Cómo interpretar los reportes?
Al correr run_test.py, se genera un archivo HTML en la carpeta principal.
El reporte incluye:
- Todos los tests ejecutados
- El estado de cada uno (passed/failed)
- El tiempo que tardó cada prueba
- Capturas de pantalla de los casos fallidos

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido utilizando Faker
- Validaciones del comportamiento en la página de inventario
- Validaciones en la página del carrito
- Pruebas de API (Reqres): GET users, POST create user, DELETE user, -Validaciones de códigos HTTP y estructura JSON

## Manejo de datos de prueba
En la carpeta datos se encuentran los archivos necesarios para alimentar las pruebas:
data_login.csv → usuarios válidos e inválidos
productos.json → información de productos para validar comportamientos

## Pruebas de API Automatizadas 
El proyecto también incluye un módulo de pruebas automatizadas de API utilizando la librería Requests, con el objetivo de validar el comportamiento de servicios externos y reforzar la calidad del flujo end-to-end desde la capa de datos.

* Cobertura de Endpoints 
Se desarrollaron al menos 3 casos de prueba sobre una API pública (por ejemplo: ReqRes), asegurando una cobertura equilibrada de los métodos HTTP más utilizados.
Métodos cubiertos:
- GET → Obtención y validación de información
- POST → Creación de recursos con datos dinámicos
- DELETE → Eliminación y verificación de respuestas
Estos endpoints permiten evaluar funcionalidades críticas dentro de cualquier sistema basado en servicios.

* Validación de Respuestas
Las pruebas incluyen verificaciones completas sobre:
Códigos de estado HTTP
Se validan respuestas como:200, 201, 204, 400, 404, entre otros.
Estructura del JSON
Se valida:
- Presencia de campos obligatorios
- Tipos de datos
- Contenido esperado
- Assertions detalladas
Cada caso de prueba cubre:
- Escenarios exitosos
- Escenarios de error
- Comparación de datos enviados vs. datos recibidos
Esto garantiza que el comportamiento del servicio sea consistente y estable ante cambios futuros.

## Integración CI/CD con GitHub Actions 
El proyecto puede integrarse fácilmente con GitHub Actions para ejecutar las pruebas de forma automática cada vez que se realiza un push o pull request al repositorio.
Funcionalidades del pipeline:
- Ejecución automática de toda la suite de pruebas
- Generación del reporte HTML dentro del pipeline
- Almacenamiento de reportes como artefactos para su posterior análisis
Esto facilita la adopción de buenas prácticas de desarrollo continuo, garantizando que cada actualización se valide de forma consistente.

### Conclusión
Este proyecto está pensado para ser una base simple, clara y adaptable para automatización de pruebas con Python y Pytest. Ofrece un flujo de ejecución accesible mediante run_test.py, con generación automática de reportes que facilitan el análisis posterior.
La arquitectura permite incorporar nuevos casos y configuraciones sin necesidad de tocar el núcleo, manteniendo buenas prácticas y asegurando que el proyecto pueda crecer de forma ordenada con el tiempo.

