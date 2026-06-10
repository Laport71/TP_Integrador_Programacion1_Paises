
# ______________________________________________________________________#
# Opcion 1 del menu principal - Carga de paises:
# la siguiente funcion agrega datos en forma de diccionario a la lista
# base_paises:

def agregar_pais():
    # se imprime los datos que debe ingresar el usuario:
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
    # el bucle while analiza el ingreso del usuario:
    while True:
        # iniciamos la captura de posibles errores:
        try:
            # se solicita una cantidad para saber cuantos paises
            # va a guardar el usuario:
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
            # se rompe el bucle
            break
    # Mantenemos un bucle activo en caso de posible error:
    while True:
        # iniciamos la captura de posibles errores:
        try:
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
                            "ingrese el nombre del pais: ").title().replace(" ", "")
                        # en caso de contener algun caracter especial o numero:
                        while nombre.isalpha() == False:
                            # se solicita nuevamente el ingreso:
                            nombre = input(
                                "Error: no puede ingresar numeros o caracteres especiales.\ningrese el nombre del pais: ").title().replace(" ", "")
                        # en caso de que el nombre ingresado ya se encuentre en la lista:
                        if any(nombre == x["pais"] for x in base_paises):
                            # generamos un error:
                            raise ValueError
                        # en caso de que el nombre no se encuentre entre los 195 paises reconocidos por la onu:
                        elif nombre not in lista_paises:
                            # se da aviso al usuario:
                            print(
                                "IMPORTANTE: estas agregando a la lista un pais que no existe,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                            # el usuario puede optar por ingresarlo de igual manera o volver a ingresar el nombre de forma correcta:
                            nuevo_pais = input(
                                "\nquieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()
                            # si el usuario no ingresa una de las opciones de forma correcta se mantendra en el bucle:
                            while nuevo_pais != "s" and nuevo_pais != "n":
                                # se informa las opciones disponibles:
                                print(
                                    "\nError: Solo puede ingresar s para SI o n para NO.")
                                # se le vuelve a repetir el mensaje de nombre extraño:
                                print(
                                    "\nIMPORTANTE: estas agregando a la lista un pais que no existe,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                                # se le pide nuevamente que ingrese una de las opciones validas:
                                nuevo_pais = input(
                                    "\nquieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()
                            # en caso de que quiera ingresarlo a la lista de todas formas a pesar de no estar entre los
                            # 195 paises reconocidos por la onu:
                            if nuevo_pais == "s":
                                break
                            # en caso de que quiera corregir el nombre:
                            elif nuevo_pais == "n":
                                # se genera un error que lo lleva a ingresar el nombre nuevamente:
                                raise TypeError
                    except TypeError:
                        # se da aviso de lo que debe realizar el usuario:
                        print("\nIngrese el nombre del pais nuevamente.\n")
                    except ValueError:
                        # se da aviso de que el pais ya se encuentra en la lista:
                        print("\nya ingreso ese pais a la lista.\n")
                    # en caso de error inesperado:
                    except Exception as e:
                        print(f"{e}")
                    # una vez que el nombre se valida de forma correcta:
                    else:
                        # se rompe el bucle
                        break
                # se le pide al usuario que ingrese los datos del pais que ingreso:
                print(f"- ingrese los datos de {nombre} -")
                # los datos que ingresa se validan mediante distintos bucles while:
                while True:
                    # inicia la captura de posibles errores:
                    try:
                        # se le solicita que ingrese la poblacion:
                        poblacion = int(input("ingrese la poblacion actual:"))
                        # el usuario no puede ingresar como poblacion 0 o un numero negativo:
                        if poblacion <= 0:
                            # en caso de que lo haga se genera un error:
                            raise ValueError
                    # si captura un error por valor:
                    except ValueError:
                        print(
                            "\nla poblacion debe ser indicada con un numero entero mayor a 0\n")
                    # en caso de error inesperado:
                    except Exception as e:
                        print(f"Error:{e}")
                    # si el ingreso se valida de forma correcta:
                    else:
                        # se rompe el bucle
                        break
                # validamos el ingreso del usuario dentro del bucle while:
                while True:
                    # inicia la captura de errores:
                    try:
                        # se le solicita al usuario un valor entero para indicar la superficie:
                        superficie = int(
                            input("Ingrese la superficie en Km²: "))
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
                # validamos el ingreso de continente:
                while True:
                    # inicia la captura de errores:
                    try:
                        # solicitamos que ingrese el continente al que pertenece el pais:
                        continente = input(
                            "Ingrese el continente en el que se encuentra: ").title().replace(" ", "")
                        # en caso de que el usuario haya ingresado un caracter especial:
                        while continente.isalpha() == False:
                            # se le solicita nuevamente que ingrese el continente:
                            continente = input(
                                f"Error: no puede ingresar numeros o caracteres especiales\ningrese el continente en el que se encuentra {nombre}: ").title().replace(" ", "")
                        # el programa utiliza el modelo de 5 continentes, el usuario tiene la posibilidad
                        # de ingresar el modelo de 7 continentes, pero se le da aviso de que el ingreso
                        # no esta dentro de la lista que valida el continente:
                        if continente not in lista_continentes:
                            print(
                                "IMPORTANTE: estas agregando a la lista un continente que no existe,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                            # el usuario tiene la posibilidad de ingresar el continente asi no este en la lista:
                            nuevo_continente = input(
                                "Quieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()
                            # validamos el ingreso del usuario solo puede ingresar s o n:
                            while nuevo_continente != "s" and nuevo_continente != "n":
                                # se le imprimen nuevamente las opciones:
                                print(
                                    "\nError: Solo puede ingresar s para SI o n para NO.")
                                print(
                                    "\nIMPORTANTE: estas agregando a la lista un continente que no existe,\nasegurate de ingresarlo de forma correcta, revisa los acentos y espacios.")
                                # se le solicita el ingreso nuevamente:
                                nuevo_continente = input(
                                    "Quieres agregarlo de todos modos? s/n: ").replace(" ", "").lower()
                            # en caso de que desee ingresar el continente de todas formas:
                            if nuevo_continente == "s":
                                break
                            # en caso de que quiera corregir su ingreso:
                            elif nuevo_continente == "n":
                                # se genera un error:
                                raise ValueError
                    # en caso de error por valor:
                    except ValueError:
                        print(f"Error: Ingrese el continente nuevamente.")
                    # una vez validado el ingreso:
                    else:
                        # se rompe el bucle
                        break
                # cuando finaliza el ingreso de paises:
                print("""
    Pais guardado con exito.
----------------------------------------------
    """)
                # guardamos los datos ingresados en la lista de diccionarios:
                base_paises.append({"pais": restaurar_palabra(nombre), "poblacion": poblacion,
                                   "superficie": superficie, "continente": restaurar_palabra(continente)})
            # damos aviso de exito al finalizar el bucle y guardar todos los datos:
            print(f"\t\nCarga exitosa.")
        # en caso de error inesperado:
        except Exception as e:
            print(f"Error inesperado:{e}")
        # en caso de finalizacion exitosa:
        else:
            # se rompe el bucle
            break

