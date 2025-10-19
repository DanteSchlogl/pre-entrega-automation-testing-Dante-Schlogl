
Tecnología,Descripción
Python,Lenguaje de programación principal.
Pytest,Framework para la ejecución y gestión de los tests.
Selenium WebDriver,Herramienta utilizada para la interacción con el navegador (automatización).
Pytest-HTML,Plugin de Pytest para generar reportes detallados en formato HTML.

Instalación y Configuración

Clonar el Repositorio:

git clone https://github.com/tu-usuario/pre-entrega-automation-testing-[dante_schlogl].git
cd pre-entrega-automation-testing-[dante_schlogl]


Instalar Dependencias:

pip install pytest pytest-html
 
intalar webdriver: https://www.youtube.com/watch?v=WQ1-0salQ4o
webdriver : https://developer.chrome.com/docs/chromedriver/get-started?hl=es-419

Ejecución de las Pruebas:
en sonsola estando en la ruta del directorio ingrasar el comando: pytest -v


Visualización del Reporte:

Una vez finalizada la ejecución, el archivo reporte.html se creará en la raíz del proyecto. Simplemente ábrelo con tu navegador para ver los resultados, incluyendo el detalle de cada prueba y las capturas de pantalla adjuntas en caso de fallo.

Evidencias Adicionales

El proyecto incluye funcionalidad para la gestión de evidencias automáticamente:

Capturas de Pantalla: Se generan capturas de pantalla de forma automática y se guardan en la carpeta screenshots/ cada vez que un caso de prueba de Pytest falla.

Reporte HTML: El reporte (reporte.html) incluye un resumen de la ejecución, el tiempo y el estado de cada test, y enlaces a las capturas de pantalla de los fallos.