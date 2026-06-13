
#Funcion que filtra por continente

def filtrar_continente():
    valida=False

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
        if filtro_continente == "Africa" or filtrar_continente=="africa":
            filtro_continente = "África"

        # Buscamos el continente en la lista estandar
        filtro_continente,valida= buscar_parecido(filtro_continente,lista_continentes)
        
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

