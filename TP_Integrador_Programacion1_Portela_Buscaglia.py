import os
###########################################################
#                                                         #
#               Trabajo Practico Integrador               #
#                   - Programacion 1 -                    #
#   Alumnos: Laura Portela c-18 - Daniel Buscaglia c-12   #
#                                                         #
###########################################################
#
# Al ejecutar este archivo .py el usuario tiene la posibilidad de
# realizar su propio registro de paises en el mundo, el programa
# guarda los datos en un archivo llamado paises.csv
# permitiendo resguardar la informacion una vez que finalice su ejecucion,
# esto le permite al usuario utilizar los datos guardados cada vez que
# lo desee.
#
#
# La variable Lista_paises contiene una tupla con los 195 países soberanos en el mundo.
# Este total se divide oficialmente en 193 Estados miembros de
# la Organización de las Naciones Unidas (ONU) y 
# 2 Estados observadores no miembros: la Santa Sede (Ciudad del Vaticano) y el Estado de Palestina
# estos datos se utilizan para validar el ingreso, en caso de un posible error, falta de ortografia o
# que el pais a agregar no se encuentre en la tupla, el usuario recibira un aviso y puede optar
# por agregarlo de todas formas o verificar el nombre para ingresarlo de forma correcta.
lista_paises = ("Afganistán", "Albania", "Alemania", "Andorra", "Angola", "AntiguaYBarbuda", "ArabiaSaudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica", "Belice", "Benín", "Bielorrusia", "Birmania", "Bolivia", "BosniaYHerzegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", "BurkinaFaso", "Burundi", "Bután", "CaboVerde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China", "Chipre", "CiudadDelVaticano", "Colombia", "Comoras", "CoreaDelNorte", "CoreaDelSur", "CostaDeMarfil", "CostaRica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto", "ElSalvador", "EmiratosÁrabesUnidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "EstadosUnidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guinea", "GuineaEcuatorial", "GuineaBisáu", "Guyana", "Haití", "Honduras", "Hungría", "India", "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "IslasMarshall", "IslasSalomón", "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano",
                "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "MacedoniaDelNorte", "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "NuevaZelanda", "Omán", "PaísesBajos", "Pakistán", "Palaos", "Palestina", "Panamá", "PapúaNuevaGuinea", "Paraguay", "Perú", "Polonia", "Portugal", "Qatar", "ReinoUnido", "RepúblicaCentroafricana", "RepúblicaCheca", "RepúblicaDelCongo", "RepúblicaDemocráticaDelCongo", "RepúblicaDominicana", "Ruanda", "Rumania", "Rusia", "Samoa", "SanCristóbalYNieves", "SanMarino", "SanVicenteYLasGranadinas", "SantaLucía", "SantoToméYPríncipe", "Senegal", "Serbia", "Seychelles", "SierraLeona", "Singapur", "Siria", "Somalia", "SriLanka", "Suazilandia", "Sudáfrica", "Sudán", "SudánDelSur", "Suecia", "Suiza", "Surinam", "Tailandia", "Taiwán", "Tanzania", "Tayikistán", "TimorOriental", "Togo", "Tonga", "TrinidadYTobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue")
#
# la variable lista_continentes contine una tupla con los datos del modelo de 5 continentes.
# Este modelo es el adoptado oficialmente por la Organización de las Naciones Unidas (ONU),
# al igual que la variable anterior la tupla es utilizada para validar el ingreso
lista_continentes = ("América", "Asia", "África", "Europa", "Oceanía")
#
# la variable base_paises contendra la lista de diccionarios con los datos que ingrese el usuario:
base_paises = []

# la siguiente funcion se encarga de validar los ingresos del usuario
# al momento de ingresar la seleccion en el menu:


def validar_opciones(seleccion):
    if seleccion.isdigit():
        print("error: valor fuera de rango")
    elif seleccion.isalpha():
        print("""
        error: 
debe ingresar un numero que exista 
dentro de las opciones del menu
""")
    else:
        print("""
        error:
    ingreso invalido
    
debe utilizar numeros para indicar
la opcion a la que desea acceder.
""")


def limpiar_pantalla():
    # 'nt' corresponde a Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux y macOS
    else:
        os.system("clear")

# Funcion que buscar palabras que tengan el mismo largo, u recorre caracter por caracter
# para buscar coincidencias , si de todas las letras solo difieren en dos ej: México y Mejico
# la toma como palabra PARECIDA y consulta al usuario si va a agregar igual


def buscar_parecido(pais, lista, valida=False):
    mejor_coincidencia = pais
    coincidencia = 0
    try:
        list_pais_ingresado = list(pais)
        list_pais_compara = []

        for p in lista:
            coincidencia = 0
            # evalua paises con igual cantidad de letras
            if len(pais) == len(p):
                list_pais_compara = list(p)

                # compara letra por letra las coincidencias
                for i in range(len(pais)):
                    if list_pais_ingresado[i] == list_pais_compara[i]:
                        coincidencia += 1

                # para nombre de paises de 1 o 2 letras ingresados. Tiene que tener al menos 1 coincidencia.
                if coincidencia >= max(1, len(pais) - 2):

                    # la mayoria de las letras coinciden entonces es un pais repetido
                    # si es falso mejor_coincidencia queda con el valor pais asignado al comienzo
                    mejor_coincidencia = p
                    valida = True
                    break

    except TypeError as e:
        print(f"Error de tipo: {e}")
        return ""
    except NameError as e:
        print(f"Error de variable no definida: {e}")
        return ""
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return ""

    # retorma si hay parecidos el nombre del pais que esta en dicc_paises y True
    # retorna si no hay parecido el pais ingresado por el usuario y False
    return mejor_coincidencia, valida

# ____________________________________________________________________________________________#
# la siguiente funcion devuelve a su estado original el pais ingresado por el usuario,
# dado que para verificarlo al principio de cada palabra se le establece una mayuscula y
# se eliminan los espacios que contiene el str.


def restaurar_palabra(pais):
    # esta variable contendra el nombre del pais ordenado con su respectivo espacio:
    nombre_ordenado = ""
    # recorremos las letras del pais al que se le quitaron los espacios
    # y se le establecio una mayuscula al inicio de cada palabra:
    for letra in pais:
        # en caso de encontrar una Y mayuscula entre medio:
        if letra.isupper() and letra == "Y" and letra != pais[0]:
            nombre_ordenado += (letra.lower())
        # si encuentra una letra mayuscula:
        elif letra.isupper() and letra != pais[0]:
            # asigna un espacio y la letra:
            nombre_ordenado += (f" {letra}")
        # si no es una letra mayuscula se agrega a la variable:
        else:
            nombre_ordenado += letra
    return nombre_ordenado


# _____________________________________________________________#
# La siguiente funcion imprime el menu principal del programa:


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


# ____________________________________________________________#
# La siguiente funcion imprime el menu de la opcion 2:


def menu_actualizar_datos():
    print("""
    -Actualizacion de poblacion o superficie-        
    
    seleccione que desea actualizar:
    1.- Poblacion
    2.- Superficie
    3.- Volver al menu principal
    """)


# ______________________________________________________________#
# La siguiente funcion imprime el menu de la opcion 4:


def menu_filtro_paises():
    print("""
        - filtro de paises -
    
    puedes filtrar los paises por:
    1.- Continente
    2.- Rango de poblacion
    3.- Rango de superficie
    4.- Volver al menu principal
    """)


# _______________________________________________________________#
# La siguiente funcion imprime el menu de la opcion 5:


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


# _________________________________________________________________#
# La siguiente funcion imprime el menu de la opcion 6:


def menu_estadisticas():
    print("""
        - estadisticas -
    
    1.- Pais con mayor y menor poblacion
    2.- Promedio de poblacion por continente
    3.- Promedio de superficie por continente
    4.- Cantidad de paises por continente
    5.- Volver al menu principal
    """)

# ______________________________________________________________________#
# Opcion 1 del menu principal - Carga de paises:
# la siguiente funcion agrega datos en forma de diccionario a la lista
# base_paises:

# Esta funcion llama a la funcion BUSCAR_PARECIDO
# Tambien usa las variables globales base_paises, lista_paises y lista_continente


def agregar_pais():
    opcion = ""
    pais_parecido = ""
    lista_paises_dicc = []
    print("""
        - Actualizacion del registro de países -

    a continuacion se le solicitara que ingrese la cantidad de paises
    que desea guardar en la base de datos, seguido de la informacion
    en el orden establecido:
    - Nombre.
    - Poblacion.
    - Superficie en Km².
    - Continente.
    """)

    # En el .csv tenemos los nombres de paises separados, lo que hago ahora es unir
    for i in base_paises:
        # Tomamos el nombre original del diccionario ("Corea del Sur")
        nombre_original = i.get("pais")

        # Lo separamos en palabras por sus espacios ["Corea del Sur"] pasa ["Corea","del","Sur"]
        palabras = nombre_original.split()

        # Forzamos primera letra mayúscula de cada palabra y unimos SIN espacios
        nombre_formateado = "".join(p[0].upper() + p[1:] for p in palabras)

        # Lo agregamos a la lista que va a usar el buscador de parecidos
        lista_paises_dicc.append(nombre_formateado)

    # PERMITE ELEGIR LA CANTIDAD DE PAISES PARA AGREGAR
    while True:
        try:
            # se solicita la cantidad de paises para agregar
            print("Cuantos paises va a agregar a la lista?")
            cantidad = int(input("ingrese la cantidad con numeros: "))

            # en caso de que ingrese 0 o un numero negativo:
            if cantidad <= 0:
                # se genera un error por mas que el ingreso sea un valor entero (int):
                raise ValueError

        # en caso de error por valor:
        except ValueError:
            print("\nError: debe ingresar un numero entero mayor a 0\n")

        # si el ingreso es valido:
        else:
            break

    # VALIDAR NOMBRE PAIS
    # en un bucle for utilizando la funcion range ingresamos la cantidad de paises
    # que va a ingresar el usuario:
    for i in range(cantidad):
        # utilizamos un bucle while para analizar el ingreso del usuario:
        while True:
            # capturamos posibles errores:
            try:
                # solicitamos el nombre del pais:
                # el nombre se estandariza con los metodos .title y .replace para analizarlo
                nombre = input(
                    f"\nIngrese el nombre del pais nro {i+1} para agregar: ").title().replace(" ", "")

                # en caso de contener algun caracter especial o numero:
                while nombre.isalpha() == False:
                    # se solicita nuevamente el ingreso:
                    nombre = input(
                        "Error: no puede ingresar numeros o caracteres especiales.\ningrese el nombre del pais: ").title().replace(" ", "")

                # en caso de que el nombre ingresado ya se encuentre en la lista:
                if any(nombre == x["pais"].replace(" ", "") for x in base_paises):
                    # generamos un error:
                    raise ValueError

                # informa que hay un pais parecido
                valida = False
                pais_parecido, valida = buscar_parecido(
                    nombre, lista_paises_dicc)
                if valida == True:
                    print(
                        f"\nEn la lista EXISTE un pais {restaurar_palabra(pais_parecido)} que es parecido")
                    elija = input(
                        f"Agrega igual a la lista {nombre} s/n: ").strip()

                    while elija != "s" and elija != "n" and elija != "S" and elija != "N":
                        elija = input(
                            "ERROR: Debe ingresar la letra S o la letra N").strip()

                    if elija == "n" or elija == "N":
                        print("El pais NO fue agregado\n")
                        # volvemos a pedir el nombre del pais actual
                        continue

                # en caso de que el nombre no se encuentre entre los 195 paises reconocidos por la onu:
                if nombre not in lista_paises:
                    # se da aviso al usuario:
                    print(
                        "\nIMPORTANTE: estas agregando a la lista un pais que NO EXISTE,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                    # el usuario puede optar por ingresarlo de igual manera o volver a ingresar el nombre de forma correcta:
                    nuevo_pais = input(
                        "\nQuieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()
                    # si el usuario no ingresa una de las opciones de forma correcta se mantendra en el bucle:
                    while nuevo_pais != "s" and nuevo_pais != "n" and nuevo_pais != "S" and nuevo_pais != "N":
                        # se informa las opciones disponibles:
                        print(
                            "\nError: Solo puede ingresar s para SI o n para NO.")
                        # se le vuelve a repetir el mensaje de nombre extraño:
                        print(
                            "\nIMPORTANTE: estas agregando a la lista un pais que NO EXISTE,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                        # se le pide nuevamente que ingrese una de las opciones validas:
                        nuevo_pais = input(
                            "\nQuieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()

                    # en caso de que quiera corregir el nombre:
                    if nuevo_pais == "n" or nuevo_pais == "N":
                        # se genera un error que lo lleva a ingresar el nombre nuevamente:
                        raise TypeError

                # si paso todas las validaciones salimos del bucle de ingreso de nombre
                break

            except TypeError:
                # se da aviso de lo que debe realizar el usuario:
                print("\nIngrese el nombre del pais nuevamente.\n")
            except ValueError:
                # se da aviso de que el pais ya se encuentra en la lista:
                print("\nEl pais ya EXISTE en la lista.\n")
            # en caso de error inesperado:
            except Exception as e:
                print(f"{e}")

        # se le pide al usuario que ingrese los datos del pais que ingreso:
        print(f"\n- ingrese los datos de {restaurar_palabra(nombre)} -")

        # VALIDAR POBLACION
        while True:
            # inicia la captura de posibles errores:
            try:
                # se le solicita que ingrese la poblacion:
                poblacion = int(input("ingrese la población actual: "))
                # el usuario no puede ingresar como poblacion 0 o un numero negativo:
                if poblacion <= 0:
                    # en caso de que lo haga se genera un error:
                    raise ValueError
            # si captura un error por valor:
            except ValueError:
                print(
                    "\nLa poblacion debe ser indicada con un numero entero mayor a 0\n")
            # en caso de error inesperado:
            except Exception as e:
                print(f"Error:{e}")
            # si el ingreso se valida de forma correcta:
            else:
                # se rompe el bucle
                break

        # VALIDAR SUPERFICIE
        while True:
            # inicia la captura de errores:
            try:
                # se le solicita al usuario un valor entero para indicar la superficie:
                superficie = int(
                    input("ingrese la superficie en Km²: "))
                # en caso de que ingrese 0 o un valor negativo:
                if superficie <= 0:
                    # generamos un error:
                    raise ValueError
            # en caso de error por valor:
            except ValueError:
                print(
                    f"Error:la superficie debe ser indicada con un numero entero mayor a 0")
            # en caso de que se valide de forma correcta:
            else:
                # se rompe el bucle:
                break

        # VALIDAR CONTINENTE
        while True:
            # solicitamos que ingrese el continente al que pertenece el pais:
            continente = input(
                "ingrese el continente en el que se encuentra: ").title().replace(" ", "")
            # en caso de que el usuario haya ingresado un caracter especial:
            while continente.isalpha() == False:
                # se le solicita nuevamente que ingrese el continente:
                continente = input(
                    f"Error: no puede ingresar numeros o caracteres especiales\ningrese el continente en el que se encuentra {restaurar_palabra(nombre)}: ").title().replace(" ", "")

            valida_cont = False
            continente_parecido, valida_cont = buscar_parecido(
                continente, lista_continentes)
            # el programa utiliza el modelo de 5 continentes, el usuario tiene la posibilidad
            # de ingresar el modelo de 7 continentes, pero se le da aviso de que el ingreso
            # no esta dentro de la lista que valida el continente:
            if continente in lista_continentes:
                break
            elif valida_cont == True and continente_parecido in lista_continentes:
                continente = continente_parecido
                break
            else:
                print("\nEl continente NO EXISTE")

        # cuando finaliza el ingreso de paises:

        print("\n     PAIS a AGREGAR \n")
        print(f"""
            pais: {restaurar_palabra(nombre)}
            poblacion: {poblacion}
            superficie: {superficie}
            continente: {continente}
            ------------------------------------------""")
        opcion = input("Confirma s/n: ")

        # pregunta si confirma el ingreso del nuevo pais

        while opcion != "s" and opcion != "n" and opcion != "S" and opcion != "N":
            opcion = input(
                "ERROR: Debe elegir la letra S para confirmar  o  N para no grabar: ")

        if opcion == "s" or opcion == "S":
            # guardamos los datos ingresados en la lista de diccionarios:
            base_paises.append({"pais": restaurar_palabra(nombre), "poblacion": poblacion,
                                "superficie": superficie, "continente": restaurar_palabra(continente)})

            # damos aviso de exito al finalizar el bucle y guardar todos los datos:
            print(f"\t\nCarga exitosa.")


# _________________________________________________________________________#
# - opcion 2 del menu principal -
# - opcion 1 dentro del menu de actualizaciones -
# la siguiente funcion permite al usuario actualizar
# los datos de poblacion de determinado pais:


def actualizar_poblacion():
    # si existe algun valor dentro de la lista:
    if base_paises:
        # solicitamos al usuario que ingrese el pais a modificar:
        print("""
            -Actualizacion de poblacion-

        ingrese el pais para actualizar su poblacion actual:""")
        # estandarizamos el ingreso para que no sea posible ingresar espacios de mas,
        # caracteres especiales o numeros:
        buscar = input("pais: ").title().replace(" ", "")
        # en caso de que haya ingresado algun caracter especial o numero:
        while buscar.isalpha() == False:
            # se imprime un aviso:
            print("Error: No puede ingresar numeros o caracteres especiales.\n")
            # solicitamos que nuevamente ingrese el pais a modificar:
            buscar = input(
                "ingrese el pais a actualizar: ").title().replace(" ", "")
        # una vez validado el ingreso devolvemos la palabra
        # restauramos el ingreso a un valor estandarizado:
        buscar = restaurar_palabra(buscar)
        # primero buscamos el pais ingresado por el usuario en la lista de diccionarios
        # con la funcion any que devuelve un valor booleano:
        if any(buscar == x["pais"] for x in base_paises):
            # en caso de que se encuentre dentro de la lista:
            # buscamos su posicion dentro del diccionario con la funcion enumerate
            # que devuelve el indice y su valor dentro de la lista:
            for posicion, i in enumerate(base_paises):
                # con el metodo get obtenemos el pais dentro del diccionario:
                pais = i.get("pais")
                # si el pais que queremos modificar se encuentra dentro del diccionario:
                if pais == buscar:
                    # iniciamos un bucle while para validar el ingreso:
                    while True:
                        # iniciamos la captura de errores:
                        try:
                            # solicitamos el nuevo numero de poblacion:
                            poblacion = int(
                                input("ingresa la poblacion actual: "))
                            # en caso de que ingrese 0 o un valor negativo:
                            if poblacion <= 0:
                                # generamos un error
                                raise ValueError
                        # en caso de error por valor:
                        except ValueError:
                            print("Error: Debe ingresar un numero entero mayor a 0")
                        # en caso de que el ingreso sea valido:
                        else:
                            # se rompe el bucle
                            break
                    # actualizamos los datos del diccionario indicando el indice, clave y su nuevo valor:
                    base_paises[posicion].update({"poblacion": poblacion})
                    actualizacion = input(
                        "Actualizacion exitosa.\npresione enter para continuar.")
        # en caso de que no se encuentre el pais en la lista de diccionarios:
        else:
            print("El pais que ingreso no se encuentra en su base de datos.")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# _______________________________________________________________________________________#
# - opcion 2 del menu principal -
# - opcion 2 dentro del menu de actualizaciones -
# la siguiente funcion permite al usuario actualizar la superficie de determinado pais:


def actualizar_superficie():
    # si existe algun valor dentro de la lista:
    if base_paises:
        # solicitamos al usuario que ingrese el pais al que se le actualizara la superficie
        print("""
            -Actualizacion de superficie-

        ingrese el pais para actualizar la superficie:""")
        # el ingreso que realiza el usuario se estandariza utilizando .title para establecer mayusculas
        # y .replace para elimiar todos los espacios:
        buscar = input("pais: ").title().replace(" ", "")
        # el bucle while se mantiene activo mientras el usuario
        # no ingrese un str sin caracteres especiales o numeros:
        while buscar.isalpha() == False:
            # se da aviso:
            print("Error: No puede ingresar numeros o caracteres especiales.\n")
            # solicitamos que ingrese el pais a buscar nuevamente:
            buscar = input(
                "ingrese el pais a actualizar: ").title().replace(" ", "")
        # restauramos el ingreso a un valor estandarizado:
        buscar = restaurar_palabra(buscar)
        # realizamos una busqueda rapida utilizando la funcion any:
        if any(buscar == x["pais"] for x in base_paises):
            # si encuentra el valor dentro de la lista de diccionarios
            # buscamos su posicion dentro del diccionario con la funcion enumerate
            # que devuelve el indice y su valor dentro de la lista:
            for posicion, i in enumerate(base_paises):
                # tomamos el valor pais que se encuentra dentro del diccionario:
                pais = i.get("pais")
                # si el pais resulta ser el que queremos modificar:
                if pais == buscar:
                    # dentro del bucle while:
                    while True:
                        # inicia la captura de errores:
                        try:
                            # solicitamos la superficie a actualizar:
                            superficie = int(
                                input("ingresa la superficie actual en Km²: "))
                            # en caso de que ingrese 0 o un numero negativo:
                            if superficie <= 0:
                                # generamos un error:
                                raise ValueError
                        # en caso de error por valor:
                        except ValueError:
                            print("Error: Debe ingresar un numero entero mayor a 0")
                        # en caso de que el ingreso sea valido:
                        else:
                            # se rompe el bucle
                            break
                    # actualizamos los datos del pais que ingreso el usuario
                    # indicando el indice, clave y nuevo valor:
                    base_paises[posicion].update({"superficie": superficie})
                    actualizacion = input(
                        "Actualizacion exitosa.\npresione enter para continuar.")
        # en caso de que no se encuentre el pais en la lista de diccionarios:
        else:
            print("El pais que ingreso no se encuentra en su base de datos.")
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ____________________________________________________________________#
# - Opcion 3 del menu principal -
# la siguiente funcion le permite al usuario buscar
# paises dentro de la lista de diccionarios:


def buscar_pais():

    lista_paises_dicc = []

    # En el .csv tenemos los nombres de paises separados, lo que hago ahora es unir
    # y creo la lista con los nombres de paises
    for i in base_paises:
        # Tomamos el nombre original del diccionario ("Corea del Sur")
        nombre_original = i.get("pais")

        # Lo separamos en palabras por sus espacios ["Corea del Sur"] pasa ["Corea","del","Sur"]
        palabras = nombre_original.split()

        # Forzamos primera letra mayúscula de cada palabra y unimos SIN espacios
        nombre_formateado = "".join(p[0].upper() + p[1:] for p in palabras)

        # Lo agregamos a la lista que va a usar el buscador de parecidos
        lista_paises_dicc.append(nombre_formateado)

    # si existe algun valor dentro de la lista:
    if base_paises:
        # indicamos al usuario las posibilidades
        # a la hora de realizar la busqueda:
        print("""
        - Busqueda de paises -

        Puedes buscar un pais en tu base de datos ingresando:
        el nombre completo o las letras que contenga el pais que buscas.
        si ingresas letras se te imprimira un listado con las coincidencias
        encontradas
        """)
        # solicitamos que ingrese el nombre o parte de el,
        # estandarizamos el ingreso utilizando los metodos .title() .replace():
        busqueda = input(
            "ingresa el pais que buscas: ").title().replace(" ", "")
        # en caso de que haya ingresado algun caracter especial o numero:
        while busqueda.isalpha() == False:
            # imprimimos el aviso:
            print("Error: no puedes ingresar caracteres especiales o numeros.")
            # solicitamos que ingrese el pais a buscar nuevamente:
            busqueda = input(
                "ingresa el nombre completo o parcial: ").title().replace(" ", "")
            busqueda = restaurar_palabra(busqueda)

        # realizamos una busqueda rapida del pais dentro del dicc (x es cada dicc de pais)
        # con la funcion any:
        if any(busqueda.lower() in x["pais"].lower() for x in base_paises):
            # en caso de que devuelva True:
            for x in base_paises:
                # recorremos los diccionarios en la lista base_paises
                # obtenemos los valores de las claves:
                pais = x.get("pais")
                poblacion = x.get("poblacion")
                superficie = x.get("superficie")
                continente = x.get("continente")
                # si lo que ingreso el usuario coincide con el nombre completo
                # o parte de el:
                if busqueda in pais:
                    # imprimimos los datos del diccionario en el que se encontro
                    # la coincidencia:
                    print(f"""
            pais: {pais}
            poblacion: {poblacion}
            superficie: {superficie}
            continente: {continente}
        ------------------------------------------""")
        # en caso de que no se encuentre el pais en la lista de diccionarios:
        else:
            print("\nNo se encuentran coincidencias exactas. Buscando parecidos...")

            # Convertimos la búsqueda al formato compacto sin espacios que espera tu función ("Corea Del Sur" -> "CoreaDelSur")
            busqueda_compacta = busqueda.replace(" ", "")

            # Pasamos 'busqueda_compacta' en lugar de 'nombre'
            pais_parecido, valida = buscar_parecido(
                busqueda_compacta, lista_paises_dicc)

            if valida == True:
                # Buscamos en qué posición de 'lista_paises_dicc' está el país parecido encontrado
                indice = lista_paises_dicc.index(pais_parecido)

                # Usamos ese mismo índice para traer los datos reales desde 'base_paises'
                datos_reales = base_paises[indice]

                print(f"""
            ¡País parecido encontrado!
            pais: {datos_reales.get('pais')}
            poblacion: {datos_reales.get('poblacion')}
            superficie: {datos_reales.get('superficie')}
            continente: {datos_reales.get('continente')}
        ------------------------------------------""")
            else:
                print("Tampoco se encontraron países lo suficientemente parecidos.")

    else:
        input("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ________________________________________________________________________#
# - opcion 4 del menu principal -
# - opcion 1 dentro del menu de filtro de paises -
# la siguiente funcion filtra los paises por continentes:


# Funcion que filtra por continente

def filtrar_continente():
    valida = False

    # si existe algun valor dentro de la lista:
    if base_paises:
        # se le pide al usuario que ingrese el continente para buscar los paises
        # que se encuentran en el:
        print("""
        - Filtro de paises por continente -
    
        ingrese el continente para imprimir los paises que pertenecen a esa region
        con los datos que corresponden a cada uno
        """)
        # el ingreso del usuario se estandariza con los metodos .title() y .replace():
        filtro_continente = input("-continente: ").title().replace(" ", "")
        # en caso de que haya ingresado un caracter especial:
        while filtro_continente.isalpha() == False:
            # imprimimos el error:
            print("error: no puede ingresar numeros o caracteres especiales.\n")
            # se solicita que ingrese el continente nuevamente:
            filtro_continente = input(
                "ingrese el continente: ").title().replace(" ", "")

        # la funcion buscar parecido  no funcionaba con Africa que tiene 6 letras,
        # si funciona con mas letras
        if filtro_continente == "Africa" or filtrar_continente == "africa":
            filtro_continente = "África"

        # Buscamos el continente en la lista estandar
        filtro_continente, valida = buscar_parecido(
            filtro_continente, lista_continentes)

        # utilizamos la funcion any para ver si se encuentra dentro de la lista de diccionarios:
        if any(filtro_continente.lower() == x["continente"].lower() for x in base_paises):
            # en caso de que devuelva True:
            print(f"Continente: {filtro_continente}")
            # recorremos la lista de diccionario:
            for x in base_paises:
                # guardamos los valores de las claves de cada diccionario:
                pais = x.get("pais")
                poblacion = x.get("poblacion")
                superficie = x.get("superficie")
                continente = x.get("continente")
                # si coincide con el continente que el usuario ingreso:
                if continente == filtro_continente:
                    # se imprime el pais con sus datos:
                    print(f"""
                    pais: {pais}
                    poblacion: {poblacion}
                    superficie: {superficie}
                    ---------------------------------""")
        # en caso de que no se encuentre el continente en la lista de diccionarios:
        else:
            print("Error: verifique la existencia del continente en la base de datos.")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# _______________________________________________________________________#
# - opcion 4 del menu principal -
# - opcion 2 dentro del menu de filtro de paises -
# la siguiente funcion filtra los paises por rango de poblacion:


def filtrar_rango_poblacion():
    # si existe algun valor dentro de la lista:
    if base_paises:
        # se le indica al usuario que valores ingresar
        # para realizar el filtro:
        print("""
        - Filtro de paises por rango de poblacion -

        ingrese el rango de poblacion para imprimir
        los paises que esten entre esos valores
        """)
        # utilizamos un bucle while para validar el ingreso:
        while True:
            # iniciamos la captura de errores:
            try:
                # solicitamos que ingrese el indice menor:
                rango_menor = int(input("poblacion minima: "))
                # en caso de que ingrese un numero negativo o 0
                if rango_menor < 0:
                    # se genera un error:
                    raise ValueError
            # en caso de error por valor:
            except ValueError:
                print("Error: No puede ingresar un numero menor a 0")
            # si el ingreso es valido:
            else:
                # se rompe el bucle
                break
        # utilizamos un bucle while para validar el ingreso:
        while True:
            # iniciamos la captura de errores:
            try:
                # solicitamos el indice mayor:
                rango_mayor = int(input("poblacion maxima: "))
                # en caso de que el indice mayor sea menor que el indice menor:
                if rango_mayor <= 0 or rango_menor > rango_mayor:
                    # se genera un error:
                    raise ValueError
            # en caso de error por valor:
            except ValueError:
                print(
                    f"Error: debe ingresar un numero mayor a 0 y superior a la poblacion minima.\n\t poblacion minima: {rango_menor}")
            # en caso de que el ingreso sea correcto:
            else:
                # se rompe el bucle
                break
        # utilizamos la funcion any para verificar que existe algun pais con ese rango de poblacion:
        if any(rango_menor <= x["poblacion"] and rango_mayor >= x["poblacion"] for x in base_paises):
            # imprimimos los valores ingresados por el usuario:
            print(
                f"paises con una poblacion entre: {rango_menor} y {rango_mayor}")
            # recorremos la lista de diccionarios para imprimir
            # los paises que se encuentran en ese rango:
            for x in base_paises:
                # obtenemos los valores de cada clave en el diccionario:
                pais = x.get("pais")
                poblacion = x.get("poblacion")
                superficie = x.get("superficie")
                continente = x.get("continente")
                # en caso de estar en el rango indicado:
                if poblacion >= rango_menor and poblacion <= rango_mayor:
                    # se imprimen todos los datos del pais relacionado:
                    print(f"""
                    pais: {pais}
                    poblacion: {poblacion}
                    superficie: {superficie}
                    continente: {continente}
                    ---------------------------------""")
        # en caso de que no exista pais entre esos valores:
        else:
            print("Error: verifique los rangos ingresados.")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# _______________________________________________________________________#
# - opcion 4 del menu principal -
# - opcion 3 dentro del menu de filtro de paises -
# la siguiente funcion filtra los paises por rango de superficie:


def filtrar_rango_superficie():
    # si existe algun valor dentro de la lista:
    if base_paises:
        print("""
        - Filtro de paises por rango de superficie -

        ingrese el rango de superficie para imprimir
        los paises que esten entre esos valores
        """)
        # validamos el ingreso del usuario:
        while True:
            # iniciamos la captura de errores:
            try:
                # solicitamos el indice menor:
                rango_menor = int(input("superficie minima: "))
                # en caso de ingresar un numero negativo o 0:
                if rango_menor < 0:
                    # se genera un error:
                    raise ValueError
            # en caso de error por valor:
            except ValueError:
                print("Error: No puede ingresar un numero menor a 0")
            # si el ingreso es valido:
            else:
                # se rompe el bucle
                break
        # validamos el ingreso del usuario utilizando un bucle while:
        while True:
            # iniciamos la captura de errores:
            try:
                # solicitamos el indice mayor:
                rango_mayor = int(input("superficie maxima: "))
                # en caso de que ingrese un numero menor al indice menor:
                if rango_mayor <= 0 or rango_menor > rango_mayor:
                    # se genera un error:
                    raise ValueError
            # en caso de error por valor:
            except ValueError:
                print(
                    f"Error: debe ingresar un numero mayor a 0 y superior a la superficie minima.\n\t superficie minima: {rango_menor}")
            # en caso de que el ingreso sea valido:
            else:
                # se rompe el bucle
                break
        # buscamos con la funcion any un pais que cumpla con el rango establecido:
        if any(rango_menor <= x["superficie"] and rango_mayor >= x["superficie"] for x in base_paises):
            # en caso de que exista:
            print(
                f"paises con una superficie entre: {rango_menor} y {rango_mayor}")
            # recorremos la lista de diccionarios:
            for x in base_paises:
                # obtenemos los valores de las claves en el diccionario
                # utilizando el metodo get:
                pais = x.get("pais")
                poblacion = x.get("poblacion")
                superficie = x.get("superficie")
                continente = x.get("continente")
                # imprimimos los paises que se encuentren dentro del rango:
                if superficie >= rango_menor and superficie <= rango_mayor:
                    print(f"""
                    pais: {pais}
                    poblacion: {poblacion}
                    superficie: {superficie}
                    continente: {continente}
                    ---------------------------------""")
        # en caso de que no se encuentre pais dentro del rango establecido:
        else:
            print("Error: verifique los rangos ingresados.")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ________________________________________________________________________________#
# - opcion 5 del menu de paises -
# - opcion 1 del menu de organizar paises -
# la siguiente funcion imprime los paises por orden alfabetico:


def orden_pais_nombre():
    # si existe alguin valor dentro de la lista:
    if base_paises:
        # creamos una lista utilizando la funcion sorted con el parametro key
        # con la funcion lambda que genera funciones en una sola linea
        # la variable x representa cada elemento dentro de la lista lo que se encuentra
        # despues de los dos puntos es lo que la funcion devuelve en este caso el valor
        # de la clave pais en el diccionario:
        base_ordenada = sorted(base_paises, key=lambda x: x["pais"])
        # imprimimos los paises que se encuentran dentro de la lista:
        print("""
        Orden de paises por nombre: """)
        # recorremos la lista de diccionarios ordenada:
        for i in base_ordenada:
            # obtenemos los valores de las claves pais y continente del diccionario con el metodo .get
            pais = i.get("pais")
            continente = i.get("continente")
            # imprimimos los valores:
            print(f"""
            pais: {pais}
            continente: {continente}
            ----------------------------""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ________________________________________________________________#
# - opcion 5 del menu de principal -
# - opcion 2 del menu de organizar paises -
# la siguiente funcion ordena los paises por poblacion:


def orden_pais_poblacion():
    # si existe algun valor dentro de la lista:
    if base_paises:
        # creamos una lista nueva utilizando el indice de poblacion
        # para ordenarla con la funcion sorted:
        base_ordenada = sorted(base_paises, key=lambda x: x["poblacion"])
        print("""
        Orden de paises por poblacion: """)
        # recorremos la lista de diccionario:
        for i in base_ordenada:
            # obtenemos los valores de las claves utilizando el metodo .get:
            pais = i.get("pais")
            poblacion = i.get("poblacion")
            continente = i.get("continente")
            # imprimimos los datos en pantalla:
            print(f"""
            pais: {pais}
            continente: {continente}
            poblacion: {poblacion}
            ----------------------------""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# __________________________________________________________________________________#
# - opcion 5 del menu de principal -
# - opcion 3 del menu de organizar paises -
# la siguiente funcion ordena los paises por superficie de forma ascendente:


def orden_pais_superficie_ascendente():
    # si existe alguin pais dentro de la lista:
    if base_paises:
        # Creamos una lista ordenada con la funcion sorted utilizando el indice
        # de superficie:
        base_ordenada = sorted(base_paises, key=lambda x: x["superficie"])
        print("""
        Orden ascendente de paises por superficie: """)
        # recorremos la lista de diccionarios:
        for i in base_ordenada:
            # obtenemos los valores de las claves utilizando el metodo get:
            pais = i.get("pais")
            superficie = i.get("superficie")
            continente = i.get("continente")
            # imprimimos los datos obtenidos:
            print(f"""
            pais: {pais}
            continente: {continente}
            superficie: {superficie}
            ----------------------------""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# __________________________________________________________________________________#
# - opcion 5 del menu de principal -
# - opcion 4 del menu de organizar paises -
# la siguiente funcion ordena los paises por superficie de forma descendente:


def orden_pais_superficie_descendente():
    # si  existe alguin pais dentro de la lista:
    if base_paises:
        # Creamos una lista ordenada con la funcion sorted esta vez
        # con el parametro reverse = True esto genera un orden descendente
        # utilizando el indice de superficie:
        base_ordenada = sorted(
            base_paises, key=lambda x: x["superficie"], reverse=True)
        print("""
        Orden descendiente de paises por superficie: """)
        # recorremos la nueva lista de diccionarios con orden descendente:
        for i in base_ordenada:
            # obtenemos los valores de las claves utilizando el metodo get:
            pais = i.get("pais")
            superficie = i.get("superficie")
            continente = i.get("continente")
            # imprimimos los datos obtenidos:
            print(f"""
            pais: {pais}
            continente: {continente}
            superficie: {superficie}
            ----------------------------""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# __________________________________________________________________________________#
# - opcion 6 del menu principal -
# - opcion 1 del menu de estadisticas -
# la siguiente funcion obtiene el pais con mayor y menor poblacion:


def estadistica_pais_poblacion():
    # si se existe alguin pais dentro de la lista:
    if base_paises:
        # las siguientes variables contienen el diccionario con mayor y menor poblacion
        # en la lista utilizando la funcion max y min respectivamente, con el parametro key
        # con la funcion lambda que genera funciones en una sola linea
        # la variable x representa cada elemento dentro de la lista lo que se encuentra
        # despues de los dos puntos es lo que la funcion devuelve en este caso el valor
        # de la clave poblacion en el diccionario:
        pais_mayor_poblacion = max(base_paises, key=lambda x: x["poblacion"])
        pais_menor_poblacion = min(base_paises, key=lambda x: x["poblacion"])
        # imprimimos todos los valores del obtenidos de cada diccionario:
        print(f"""
-------------------------------------------------------------------------------------------
        
        el pais con menor poblacion es: {pais_menor_poblacion["pais"]}
        se encuentra en el continente: {pais_menor_poblacion["continente"]}
        tiene una poblacion de: {pais_menor_poblacion["poblacion"]} habitantes
        en una superficie de: {pais_menor_poblacion["superficie"]} Km²

        el pais con mayor poblacion es: {pais_mayor_poblacion["pais"]}
        se encuentra en el continente: {pais_mayor_poblacion["continente"]}
        tiene una poblacion de: {pais_mayor_poblacion["poblacion"]} habitantes
        en una superficie de: {pais_mayor_poblacion["superficie"]} Km²

--------------------------------------------------------------------------------------------
        """)
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ______________________________________________________________________________#
# - opcion 6 del menu principal -
# - opcion 2 del menu de estadisticas -
# la siguiente funcion obtiene el promedio de poblacion por continente:


def promedio_poblacion_continente():
    # si existe alguin pais dentro de la lista:
    if base_paises:
        # primero se obtienen todos los continentes dentro de la lista de diccionarios
        # se guardan dentro de la lista continentes:
        continentes = []
        # se crea una lista que es corelativa a la lista continentes:
        suma_poblacion_continente = []
        # recorremos la lista de diccionarios:
        for x in base_paises:
            # obtenemos el valor de la clave "continente"
            continente = x.get("continente")
            # si no se encuentra dentro de la lista:
            if continente not in continentes:
                # lo guardamos
                continentes.append(continente)
        # una vez obtenidos todos los continentes dentro de la lista de diccionarios:
        # recorremos la lista continentes:
        for x in continentes:
            # creamos una variable para sumar los paises:
            suma_pais = 0
            # creamos una variable para sumar la poblacion de cada pais dentro del continente
            # que se esta analizando:
            suma_poblacion = 0
            # iniciamos un recorrido por la lista de diccionario para comparar los datos:
            for i in base_paises:
                # obtenemos el valor de la clave "continente"
                continente = i.get("continente")
                # obtenemos el valor de la clave "poblacion"
                poblacion = i.get("poblacion")
                # si el continente en la lista es igual al del diccionario que estamos analizando
                if continente == x:
                    # sumamos un pais:
                    suma_pais += 1
                    # sumamos la poblacion del continente:
                    suma_poblacion += poblacion
            # al finalizar el recorrido de la lista de diccionarios:
            # dividimos la suma total de la poblacion
            # por el total de paises dentro del continente
            # eso nos da el promedio:
            promedio = suma_poblacion / suma_pais
            # guardamos el promedio en la lista:
            suma_poblacion_continente.append(promedio)
        # imprimimos toda la informacion que obtuvimos analizando los datos:
        print("""
        - Promedio de poblacion por continente -
        """)
        # dado que las listas continentes y suma_poblacion_continente son correlativas
        # lo que se encuentra en la posicion 0 de una hace referencia a lo que se encuentra
        # en la posicion 0 de la otra:
        # obtenemos la informacion utilizando un bucle for con las funciones range, len():
        for i in range(len(continentes)):
            # imprimimos los datos obtenidos:
            print(f"""
        continente: {continentes[i]} promedio de poblacion: {suma_poblacion_continente[i]}""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# _____________________________________________________________________________#
# - opcion 6 del menu de principal -
# - opcion 3 del menu de organizar paises -
# la siguiente funcion obtiene el promedio de superficie por continente:


def promedio_superficie_continente():
    # si se existe alguin pais dentro de la lista:
    if base_paises:
        # primero se obtienen todos los continentes dentro de la lista de diccionarios
        # se guardan dentro de la lista continentes:
        continentes = []
        # se crea una lista que es corelativa a la lista continentes:
        suma_superficie_continente = []
        # recorremos la lista de diccionarios:
        for x in base_paises:
            # obtenemos el valor de la clave "continente"
            continente = x.get("continente")
            # si no se encuentra dentro de la lista:
            if continente not in continentes:
                # lo guardamos
                continentes.append(continente)
        # una vez obtenidos todos los continentes dentro de la lista de diccionarios:
        # recorremos la lista continentes:
        for x in continentes:
            # creamos una variable para sumar los paises:
            suma_pais = 0
            # creamos una variable para sumar la superficie de cada pais dentro del continente
            # que se esta analizando:
            suma_superficie = 0
            # iniciamos un recorrido por la lista de diccionario para comparar los datos:
            for i in base_paises:
                # obtenemos el valor de la clave "continente"
                continente = i.get("continente")
                # obtenemos el valor de la clave "superficie"
                superficie = i.get("superficie")
                # si el continente en la lista es igual al del diccionario que estamos analizando
                if continente == x:
                    # sumamos un pais:
                    suma_pais += 1
                    # sumamos la superficie del continente:
                    suma_superficie += superficie
            # al finalizar el recorrido de la lista de diccionarios:
            # dividimos la suma total de la superficie
            # por el total de paises dentro del continente
            # eso nos da el promedio:
            promedio = suma_superficie / suma_pais
            # guardamos el promedio en la lista:
            suma_superficie_continente.append(promedio)
        # imprimimos toda la informacion que obtuvimos analizando los datos:
        print("""
        - Promedio de poblacion por continente -
        """)
        # dado que las listas continentes y suma_superficie_continente son correlativas
        # lo que se encuentra en la posicion 0 de una hace referencia a lo que se encuentra
        # en la posicion 0 de la otra:
        # obtenemos la informacion utilizando un bucle for con las funciones range, len():
        for i in range(len(continentes)):
            # imprimimos los datos obtenidos:
            print(f"""
        continente: {continentes[i]} promedio de superficie: {suma_superficie_continente[i]}""")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")


# ______________________________________________________________________________________________#
# - opcion 6 del menu de principal -
# - opcion 4 del menu de estadisticas -
# la siguiente funcion muestra la cantidad y los paises que tiene cada continente

def cantidad_paises_continente():
    # si se existe alguin pais dentro de la lista:
    if base_paises:
        # creamos una lista con los posibles continentes dentro de la lista de diccionarios:
        continentes = []
        for x in base_paises:
            # recorremos la lista y obtenemos el valor de la clave "continente"
            continente = x.get("continente")
            # si no se encuentra en la lista:
            if continente not in continentes:
                # se guarda el nombre en la lista continentes:
                continentes.append(continente)
        # luego de obtener todos los continentes dentro de la lista
        # recorremos la lista de diccionarios con un bucle for:
        for x in continentes:
            # generamos una lista paises para ir contando cuantos paises contiene cada continente:
            paises = []
            # imprimimos el nombre del continente que analizamos:
            print(f"""
            Paises del continente: {x}""")
            # recorremos la lista de diccionario y comparamos los valores de las dos listas:
            for i in base_paises:
                # guardamos el valor de la clave "continente" dentro de la lista de diccionarios:
                continente = i.get("continente")
                # guardamos el valor de la clave "pais" dentro de la lista de diccionarios:
                pais = i.get("pais")
                # si el continente coincide en las dos listas:
                if continente == x:
                    # guardamos el pais en la lista:
                    paises.append(pais)
                    # mostramos los paises que contiene ese continente:
                    print(pais, end="")
            # imprimimos el numero total de paises que contiene cada continente al finalizar el recorrido:
            print(f"{x} cuenta en total con {len(paises)} paises")
            print("--------------------------------------------------------")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")

# _________________________CODIGO PRINCIPAL ___________________________________#


# Inicia el programa:
limpiar_pantalla()
print("-"*80)
print("                          SISTEMA DE GESTION DE PAISES")
print("-"*80)

print("""
    - B I E N V E N I D O !

    - Este es tu registro de paises en el mundo,
      si es la primera vez que inicias este programa
      deberas realizar la carga de paises con la opcion 1
      del menu.
""")
print("-"*80)
# Abrimos el archivo "paises.csv" en modo lectura:
try:
    with open("paises.csv", "r", encoding="utf-8")as archivo:
        # saltamos la primera linea que contiene nombre de campos
        next(archivo)

        # recorremos las siguientes lineas en el archivo
        # para armar la lista de diccionario
        for i in archivo:
            # analizamos el contenido de cada linea separando los valores dentro de una lista:
            contenido_linea = i.strip().split(",")
            poblacion = int(contenido_linea[1])
            superficie = int(contenido_linea[2])

            # creamos un diccionario con los datos de la lista:
            dic_paises = {
                "pais": contenido_linea[0], "poblacion": poblacion, "superficie": superficie, "continente": contenido_linea[3]}

            # guardamos cada diccionario en la lista de diccionarios:
            base_paises.append(dic_paises)

# en caso de que no exista el archivo y se genere un error:
except FileNotFoundError:
    # creamos el archivo con la linea necesaria para la comprencion del archivo csv:
    with open("paises.csv", "w", encoding="utf-8")as archivo:
        archivo.writelines("nombre,poblacion,superficie,continente\n")

# MENU PRINCIPAL dentro de un bucle while que se repetira
# hasta que el usuario desee salir:
while True:
    try:
        # imprimimos el menu principal:
        menu_inicio()

        # pedimos al usuario que ingrese una opcion del menu principal:
        seleccion_menu_principal = input(
            "ingrese una de las opciones: ").replace(" ", "")

        # OPCION 1 - MENU CARGAR PAIS
        if seleccion_menu_principal == "1":
            limpiar_pantalla()
            agregar_pais()

        # OPCION 2 - MENU ACTUALIZAR DATOS
        elif seleccion_menu_principal == "2":
            limpiar_pantalla()
            # dentro de un bucle while el SUBMENU de ACTUALIZAR DATOS:
            while True:
                menu_actualizar_datos()
                # Validamos opcion del submenu
                seleccion_actualizar_datos = input(
                    "ingrese la opcion: ").replace(" ", "")

                # OPCION 1- SUBMENU ACTUALIZAR POBLACION
                if seleccion_actualizar_datos == "1":
                    limpiar_pantalla()
                    actualizar_poblacion()

                # OPCION 2- SUBMENU ACTUALIZAR SUPERFICIE
                elif seleccion_actualizar_datos == "2":
                    limpiar_pantalla()
                    actualizar_superficie()

                # OPCION 3- SUBMENU VOLVER AL MENU PRINCIPAL
                elif seleccion_actualizar_datos == "3":
                    limpiar_pantalla()
                    break

                # en caso de ingresar un numero fuera del rango:
                else:
                    validar_opciones(seleccion_actualizar_datos)

        # OPCION 3 - MENU BUSCAR PAIS
        elif seleccion_menu_principal == "3":
            limpiar_pantalla()
            buscar_pais()

        # OPCION 4 - MENU FILTRAR PAIS
        elif seleccion_menu_principal == "4":
            limpiar_pantalla()

            while True:
                # imprimimos el menu de filtro de paises:
                menu_filtro_paises()

                # solicitamos al usuario que ingrese una opcion:
                seleccion_filtro = input(
                    "ingrese una de las opciones:").replace(" ", "")

                # OPCION 1- SUBMENU FILTRAR POR CONTINENTE
                if seleccion_filtro == "1":
                    limpiar_pantalla()
                    filtrar_continente()

                # # OPCION 2 - SUBMENU FILTRAR POR RANGO POBLACION
                elif seleccion_filtro == "2":
                    limpiar_pantalla()
                    filtrar_rango_poblacion()

                # OPCION 3- SUBMENU FILTRAR POR SUPERFICIE
                elif seleccion_filtro == "3":
                    limpiar_pantalla()
                    filtrar_rango_superficie()

                # OPCION 4- SUBMENU VOLVER AL MENU PRINCIPAL
                elif seleccion_filtro == "4":
                    limpiar_pantalla()
                    break

                # en caso de ingresar un valor fuera del rango:
                else:
                    validar_opciones(seleccion_filtro)

        # OPCION 5 - MENU ORDENAR
        elif seleccion_menu_principal == "5":
            limpiar_pantalla()

            while True:
                # imprimimos el menu de organizar paises:
                menu_orden_pais()
                # solicitamos al usuario que ingrese una opcion:
                seleccion_orden_pais = input(
                    "ingrese una de las opciones: ").replace(" ", "")

                # OPCION 1 - SUBMENU ORDENAR POR NOMBRE DE PAIS
                if seleccion_orden_pais == "1":
                    limpiar_pantalla()
                    orden_pais_nombre()

                # OPCION 2 - SUBMENU ORDENAR POR POBLACION
                elif seleccion_orden_pais == "2":
                    limpiar_pantalla()
                    orden_pais_poblacion()

                # OPCION 3 - SUBMENU ORDENAR POR SUPERFICIE ASCENDENTE
                elif seleccion_orden_pais == "3":
                    limpiar_pantalla()
                    orden_pais_superficie_ascendente()

                # OPCION 4 - SUBMENU ORDENAR POR SUPERFICIE DESCENDENTE
                elif seleccion_orden_pais == "4":
                    limpiar_pantalla()
                    orden_pais_superficie_descendente()

                # OPCION 5 - SUBMENU VOLVER AL MENU PRINCIPAL
                elif seleccion_orden_pais == "5":
                    break

                # en caso de ingresar un valor fuera de rango:
                else:
                    validar_opciones(seleccion_orden_pais)

        # OPCION 6 - MENU ESTADISTICAS
        elif seleccion_menu_principal == "6":
            limpiar_pantalla()

            # dentro de un bucle while:
            while True:
                menu_estadisticas()
                # solicitamos al usuario que ingrese una opcion:
                seleccion_menu_estadisticas = input(
                    "ingrese una de las opciones: ").replace(" ", "")

                # OPCION 1 - SUBMENU ESTADISTICA POR POBLACION
                if seleccion_menu_estadisticas == "1":
                    limpiar_pantalla()
                    estadistica_pais_poblacion()

                # OPCION 2 - SUBMENU ESTADISTICA POR CONTINENTE
                elif seleccion_menu_estadisticas == "2":
                    limpiar_pantalla()
                    promedio_poblacion_continente()

                # OPCION 3 - SUBMENU ESTADISTICA PROMEDIO SUPERFICIE
                elif seleccion_menu_estadisticas == "3":
                    limpiar_pantalla()
                    promedio_superficie_continente()

                # OPCION 4 - SUBMENU ESTADISTICA POR CANTIDAD DE PAISES X CONTINENTE
                elif seleccion_menu_estadisticas == "4":
                    limpiar_pantalla()
                    cantidad_paises_continente()

                # OPCION 5 - SUBMENU VOLVER AL MENU PRINCIPAL
                elif seleccion_menu_estadisticas == "5":
                    break

                # en caso de ingresar un valor fuera de rango:
                else:
                    validar_opciones(seleccion_menu_estadisticas)

        # OPCION 7 - MENU SALIR
        elif seleccion_menu_principal == "7":
            break

        # en caso de valor fuera de rango en menu principal:
        else:
            validar_opciones(seleccion_menu_principal)

    # en caso de error inesperado:
    except Exception as e:
        print(f"Error inesperado: {e}")

    # este bloque se ejecuta al finalizar cualquier accion en el menu principal:
    finally:
        # esta accion SOBREESCRIBE el archivo para actualizar
        # cualquier posible modificacion realizada por el usuario
        # abrimos el archivo paises.csv:
        with open("paises.csv", "w", encoding="utf-8")as archivo:
            # escribimos la primera linea para identificar la informacion
            # dentro del archivo csv para su comprencion:
            archivo.writelines("nombre,poblacion,superficie,continente\n")

            # recorremos la lista de diccionarios:
            for x in base_paises:
                # obtenemos el valor de cada clave dentro del diccionario:
                nombre = x.get("pais")
                poblacion = x.get("poblacion")
                superficie = x.get("superficie")
                continente = x.get("continente")

                # guardamos la informacion dentro del archivo:
                archivo.writelines(
                    f"{nombre},{poblacion},{superficie},{continente}\n")
