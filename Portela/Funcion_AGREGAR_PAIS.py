# ______________________________________________________________________#
# Opcion 1 del menu principal - Carga de paises:
# la siguiente funcion agrega datos en forma de diccionario a la lista
# base_paises:

# Esta funcion llama a la funcion BUSCAR_PARECIDO
# Tambien usa las variables globales base_paises, lista_paises y lista_continente

def agregar_pais():
    opcion=""
    pais_parecido=""    
    lista_paises_dicc=[]
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
                nombre = input(f"\nIngrese el nombre del pais nro {i+1} para agregar: ").title().replace(" ", "")
                
                # en caso de contener algun caracter especial o numero:
                while nombre.isalpha() == False:
                    # se solicita nuevamente el ingreso:
                    nombre = input(
                        "Error: no puede ingresar numeros o caracteres especiales.\ningrese el nombre del pais: ").title().replace(" ", "")


                # en caso de que el nombre ingresado ya se encuentre en la lista:
                if any(nombre == x["pais"].replace(" ","") for x in base_paises):
                    # generamos un error:
                    raise ValueError
                
                # informa que hay un pais parecido
                valida=False
                pais_parecido,valida = buscar_parecido(nombre,lista_paises_dicc)
                if valida==True:
                    print(f"\nEn la lista EXISTE un pais {restaurar_palabra(pais_parecido)} que es parecido")
                    elija = input(f"Agrega igual a la lista {nombre} s/n: ").strip()
                    
                    while elija !="s" and elija !="n" and elija !="S" and elija !="N" :
                        elija= input("ERROR: Debe ingresar la letra S o la letra N").strip()
                    
                    if elija=="n" or elija=="N":
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
                    if nuevo_pais == "n" or nuevo_pais == "N" :
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
            
            valida_cont=False
            continente_parecido,valida_cont = buscar_parecido(continente,lista_continentes)
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
       
        while opcion !="s" and opcion !="n" and opcion !="S" and opcion !="N" :
            opcion = input ("ERROR: Debe elegir la letra S para confirmar  o  N para no grabar: " )

        if opcion =="s" or opcion=="S":
            # guardamos los datos ingresados en la lista de diccionarios:
            base_paises.append({"pais": restaurar_palabra(nombre), "poblacion": poblacion,
                            "superficie": superficie, "continente": restaurar_palabra(continente)})
        
            # damos aviso de exito al finalizar el bucle y guardar todos los datos:
            print(f"\t\nCarga exitosa.")
