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
