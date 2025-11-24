# Entrega Final de Proyecto: Framework de Automatización de Pruebas

Este proyecto consiste en un framework de testing automatizado híbrido desarrollado en Python. Combina pruebas de UI (Interfaz de Usuario) utilizando **Selenium WebDriver** con el patrón de diseño **Page Object Model (POM)**, y pruebas de API utilizando la librería **Requests**.

## 🛠️ Tecnologías Utilizadas

| Tecnología | Descripción |
|------------|-------------|
| **Python** | Lenguaje de programación principal. |
| **Pytest** | Framework para la ejecución, gestión de tests y assertions. |
| **Selenium WebDriver** | Automatización de interacción con el navegador (UI). |
| **Requests** | Librería para realizar peticiones HTTP y probar APIs REST. |
| **Pytest-HTML** | Generación de reportes visuales detallados. |
| **Page Object Model** | Patrón de diseño para estructurar el código de UI de manera escalable. |

## 📂 Organización del Proyecto

El código está organizado siguiendo buenas prácticas de modularización:

* `pages/`: Clases del Page Object Model (Lógica de las páginas web).
* `tests/`: Scripts de prueba (UI y API).
* `utils/`: Herramientas comunes y cargadores de datos.
* `data/`: Archivos JSON con datos de prueba (Data Driven Testing).
* `reports/`: Resultados de las ejecuciones (HTML y Screenshots).

## ⚙️ Instalación y Configuración

1. **Clonar el Repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/pre-entrega-automation-testing-](https://github.com/tu-usuario/pre-entrega-automation-testing-)[dante_schlogl].git
   cd pre-entrega-automation-testing-[dante_schlogl]