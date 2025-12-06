#Proyecto de Talento Tech

##Propósito del proyecto
Este proyecto nace con la idea de practicar y consolidar habilidades de automatización, aplicando pruebas de UI y API sobre el sitio SauceDemo. La intención no es solo automatizar, sino también construir una base sólida con buenas prácticas como Page Object Model, manejo de datos externos, generación automática de reportes, logs claros y evidencias visuales para cada prueba fallida.

##Tecnologías utilizadas
-Python 3.x
-Pytest
-Selenium WebDriver
-Logging
-Faker
-CSV / JSON
-Requests

###Reportes y Logs
Durante la ejecución, el proyecto genera diferentes tipos de resultados que ayudan tanto al análisis técnico como al seguimiento del proceso: reporte HTML, capturas de pantalla y archivo de logs.

##Reporte HTML
Al finalizar la ejecución, se crea un archivo reporte.html en la carpeta raíz, donde se puede ver el detalle de cada caso de prueba: su estado, duración y cualquier evidencia disponible.

##Logs de ejecución
Se registra toda la actividad de las pruebas en el archivo:
logs/suite.log
Este archivo permite entender qué ocurrió internamente durante la ejecución, facilitando el análisis y la trazabilidad.


##Capturas de pantalla
Cuando una prueba falla, se guarda automáticamente una captura en:
reports/screens/
Estas evidencias visuales ayudan a identificar rápidamente qué salió mal.

##Ejecutar todas las pruebas
Para ejecutar toda la suite de pruebas, simplemente corré:
python -m run_test.py

##¿Cómo interpretar los reportes?
Al correr run_test.py, se genera un archivo HTML en la carpeta principal.
El reporte incluye:
-Todos los tests ejecutados
-El estado de cada uno (passed/failed)
-El tiempo que tardó cada prueba
-Capturas de pantalla de los casos fallidos

##Pruebas incluidas
-Login exitoso y fallido
-Login exitoso y fallido utilizando Faker
-Validaciones del comportamiento en la página de inventario
-Validaciones en la página del carrito
-Pruebas de API (Reqres): GET users, POST create user, DELETE user, -Validaciones de códigos HTTP y estructura JSON

##Manejo de datos de prueba
En la carpeta datos se encuentran los archivos necesarios para alimentar las pruebas:
data_login.csv → usuarios válidos e inválidos
productos.json → información de productos para validar comportamientos

###Conclusión
Este proyecto está pensado para ser una base simple, clara y adaptable para automatización de pruebas con Python y Pytest. Ofrece un flujo de ejecución accesible mediante run_test.py, con generación automática de reportes que facilitan el análisis posterior.
La arquitectura permite incorporar nuevos casos y configuraciones sin necesidad de tocar el núcleo, manteniendo buenas prácticas y asegurando que el proyecto pueda crecer de forma ordenada con el tiempo.
 (docs: actualizar README con mejoras en la documentación)
