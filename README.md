import os

# Definimos el contenido estructurado del README.md basado en todo el contexto del TP de Laura y Daniel
readme_content = """# Sistema de Gestión de Datos de Países 🌍

¡Bienvenido al repositorio del Trabajo Práctico Integrador de Programación 1! Este proyecto consiste en una aplicación de consola interactiva desarrollada en **Python** que permite registrar, gestionar y analizar datos geográficos, demográficos y estadísticos de diferentes países del mundo, utilizando un archivo **CSV** para garantizar la persistencia de los datos.

## 👥 Integrantes
* **Laura Analía Portela** (Comisión 18) - *UTN TUPaD*
* **Daniel Elías Buscaglia** (Comisión 12) - *UTN TUPaD*

## 🚀 Link Video de Youtube y Link al Repositorio
Repositorio en GitHub: 
[  https://github.com/Laport71/TP_Integrador_Programacion1_Paises  ]

Video Demostrativo: 
[ https://www.youtube.com/watch?v=RPVDURkQGKg&t=1s ]

Documentacion PDF:
https://github.com/Laport71/TP_Integrador_Programacion1_Paises/blob/main/Trabajo_Integrador_Promacion1_Laura_Portela_Daniel_Buscaglia.pdf

## 🛠️ Tecnologias utilizadas

•	Lenguaje: Python 3.x
•	Estructuras de datos: Listas y Diccionarios.
•	Persistencia: Manejo de archivos CSV.
•	Control de Versiones: Git y GitHub.


## 🚀 Características Principales

* **Persistencia de Datos (CSV):** Carga automática al iniciar el programa y guardado seguro al salir en `paises.csv`. Control de errores si el archivo no existe en la primera ejecución (`FileNotFoundError`).
* **Validación Estricta:** Control riguroso de ingresos de datos para evitar caídas del sistema (bloqueo de letras en campos numéricos y caracteres inválidos en campos de texto).
* **Filtrado Avanzado:** Consulta de países por continente, rangos de población y rangos de superficie.
* **Ordenamiento Dinámico:** Capacidad de ordenar la base de datos por nombre, población o superficie (ascendente y descendente) utilizando expresiones `lambda`.
* **Módulo Estadístico:** * Identificación del país con mayor y menor población.
    * Promedio de población por continente.
    * Promedio de superficie por continente.
    * Conteo exacto y listado de países por continente.
* **Buscador Flexible:** Búsqueda por coincidencia exacta o parcial, ignorando mayúsculas/minúsculas y espacios (ej. busca "Costa Rica" de forma exitosa aunque se ingrese "costarica").

---

## 🛠️ Estructura y Decisiones Técnicas

* **Estructura Principal:** Se utiliza una **lista de diccionarios** (`base_paises`) como el núcleo dinámico de almacenamiento en memoria RAM.
* **Estandarización y Normalización:** Implementación de la función a medida `restaurar_palabra()` para formatear los nombres guardados y garantizar la consistencia en las búsquedas evitando errores de claves (`KeyError`).
* **Modularización:** Código limpio y ordenado dividido enteramente en funciones específicas reutilizables.
* **Interfaz Limpia:** Incorporación de rutinas de limpieza de pantalla (`os.system`) adaptativas para sistemas operativos Windows (`nt`) y basados en Unix/Linux/macOS.

## 🛠️ Contribuciones de los integrantes

* **Daniel Buscaglia** (Comisión 12) - *UTN TUPaD*
  * **Estructura Principal y Flujo del Sistema:** Diseñó la arquitectura central del script, implementando el bucle global de ejecución, el enrutamiento de funciones según la opción seleccionada y la persistencia de datos (apertura, lectura inicial y sobreescritura automatizada en el archivo `paises.csv` mediante bloques de control).
  * **Arquitectura de Interfaz y Navegación:** Desarrolló el sistema modular de menús (principal y submenús) e implementó la función `validar_opciones` con `.isdigit()` y `.isalpha()` para prevenir ingresos inválidos de control.
  * **Procesamiento de Cadenas (UX):** Desarrolló el algoritmo `restaurar_palabra` para decodificar textos en formato compacto e inyectar automáticamente los espacios legibles en pantalla.
  * **Módulo de Modificación y Filtros:** Programó la lógica para la reescritura en memoria de poblaciones y superficies, y diseñó el sistema de filtrado avanzado por rangos numéricos acotados (mínimos y máximos).
  * **Módulo Estadístico y Ordenamiento (Analítica):** Implementó el uso avanzado de `lambda`, `max()`, `min()` y `sorted()` para identificar valores críticos y clasificar datos (alfabético, poblacional y territorial). Desarrolló los algoritmos para calcular promedios por continente y el conteo/agrupación geográfica.

  
  * **Laura Analía Portela** (Comisión 12) - *UTN TUPaD*
  * **Contribución:** Desarrollo del **Módulo de Gestión, Búsqueda y Validación de Datos**.
    * **Robustez en Carga de Datos:** Implementó la función `agregar_pais` con un sistema estricto de captura de excepciones (`try-except`, `ValueError`, `TypeError`) para evitar el ingreso de datos nulos, números negativos o tipos incorrectos en poblaciones y superficies.
    * **Algoritmo de Coincidencias Óptimas:** Diseñó y optimizó la lógica de `buscar_parecido`, un algoritmo propio que evalúa cadenas de texto basándose en su longitud y concordancia de caracteres posicionales para detectar duplicados implícitos o errores de tipeo (ej. "México" vs "Mejico").
    * **Estandarización y Formateo:** Desarrolló los mecanismos de normalización de cadenas de texto mediante manipulación de strings (`.title()`, `.replace()`, `.split()`) para garantizar que las búsquedas y los filtros sean agnósticos a los espacios y mayúsculas.
    * **Módulos de Consulta Dinámica:** Programó las funciones de búsqueda parcial/total (`buscar_pais`) y el sistema de segmentación regional (`filtrar_continente`), integrando estructuras de control eficientes como la función integrada `any()` para optimizar el recorrido de la base de datos distribuida en diccionarios.


## 📋 Diccionario de Datos

### Variables Globales

| Variable            | Tipo          | Descripción 
|---------------      |---------------|-------------
| `base_paises`       | `list[dict]`  | Estructura principal del programa. Lista de diccionarios cada elemento representa un país.
| `lista_paises`      | `list[str]`   | Lista con los 195 países.Se usa para validar el nombre ingresado por el usuario.
| `lista_continentes` | `list[str]`   | Lista con los 5 continentes. Se usa para validar el continente ingresado. 

### Estructura de cada elemento en `base_paises`

Cada país se almacena como un diccionario con la siguiente forma:

```python
{"pais": "Argentina", "poblacion": 46000000, "superficie": 2780400, "continente": "América"}


| Clave         | Tipo  | Descripción 
|---------------|-------|
| `"pais"`      | `str` | Nombre del país 
| `"poblacion"` | `int` | Cantidad de pobladores
| `"superficie"`| `int` | Superficie del país  en Km². 
| `"continente"`| `str` | Nombre del Continente.

### Archivo de persistencia

| Archivo      | Formato | Descripción |
|--------------|---------|
| `paises.csv` | CSV     | Almacena los datos de `base_paises` entre ejecuciones. 


## ⚙️ Requisitos e Instalación

1. Tener instalado **Python 3.x** en tu sistema.
2. Clonar este repositorio e ingresar a la carpeta del proyecto:

```bash
# Clonar el repositorio
git clone [https://github.com/Laport71/TP_Integrador_Programacion1_Paises](https://github.com/Laport71/TP_Integrador_Programacion1_Paises)

# Entrar al directorio del proyecto
cd TP_Integrador_Programacion1_Paises


## 🎮 Modo de Uso

Para iniciar la aplicación, ejecuta el script principal desde tu terminal o consola de comandos:

```bash
python TP_Integrador-programacion.py

El archivo paises.csv tiene que estar en el mismo directorio del archivo .py