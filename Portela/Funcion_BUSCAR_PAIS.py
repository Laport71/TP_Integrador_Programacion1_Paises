
# ____________________________________________________________________#
# - Opcion 3 del menu principal -
# la siguiente funcion le permite al usuario buscar
# paises dentro de la lista de diccionarios:


def buscar_pais():

    lista_paises_dicc=[]

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
            pais_parecido, valida = buscar_parecido(busqueda_compacta, lista_paises_dicc)
            
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
        
    

