def menu_inicio():
    print("""
        Opciones del menu principal:

    1.- Agregar países a la base de datos
    2.- Actualizar los datos de Población y Superficie de un País
    3.- Buscar un país por nombre (coincidencia parcial o exacta)
    4.- Filtrar países
    5.- Ordenar países
    6.- Mostrar estadisticas.
    7.- Salir
    """)


def menu_actualizar_datos():
    print("""
    -Actualizacion de poblacion o superficie-        
    
    seleccione que desea actualizar:
    1.- Poblacion
    2.- Superficie
    3.- Volver al menu principal
    """)


def menu_filtro_paises():
    print("""
        - filtro de paises -
    
    puedes filtrar los paises por:
    1.- Continente
    2.- Rango de poblacion
    3.- Rango de superficie
    4.- Volver al menu principal
    """)


def menu_orden_pais():
    print("""
        - Organizar paises -
    
    puedes ordenados por:
    1.- Nombre
    2.- Poblacion
    3.- superficie orden ascendente
    4.- superficie orden descendente
    5.- Volver al menu principal
    """)


def menu_estadisticas():
    print("""
        - estadisticas -
    
    1.- Pais con mayor y menor poblacion
    2.- Promedio de poblacion por continente
    3.- Promedio de superficie por continente
    4.- Cantidad de paises por continente
    5.- Volver al menu principal
    """)
