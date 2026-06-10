# ____________________________________________________________________#
# - Opcion 3 del menu principal -
# la siguiente funcion le permite al usuario buscar
# paises dentro de la lista de diccionarios:


def buscar_pais():
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
        # realizamos una busqueda rapida con la funcion any:
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
            print("No se encuentran coincidencias en su base de datos.")
    # en caso de que no haya valores dentro de la lista de diccionarios:
    else:
        print("Error: debe ingresar al menos 1 pais a la lista utilizando la opcion 1 del menu.")

