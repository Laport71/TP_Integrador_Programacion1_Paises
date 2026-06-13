# Funcion que buscar palabras que tengan el mismo largo, u recorre caracter por caracter
# para buscar coincidencias , si de todas las letras solo difieren en dos ej: México y Mejico
# la toma como palabra PARECIDA y consulta al usuario si va a agregar igual

def buscar_parecido(pais,lista,valida=False):
    mejor_coincidencia = pais
    coincidencia=0
    try:
        list_pais_ingresado=list(pais)
        list_pais_compara=[]
        
        for p in lista:
            coincidencia=0
            # evalua paises con igual cantidad de letras 
            if len(pais) == len(p):
                list_pais_compara = list(p)

                # compara letra por letra las coincidencias
                for i in range(len(pais)):
                    if list_pais_ingresado[i]== list_pais_compara[i]:
                        coincidencia += 1
                
                # para nombre de paises de 1 o 2 letras ingresados. Tiene que tener al menos 1 coincidencia.
                if coincidencia >= max(1, len(pais) - 2):

                    #la mayoria de las letras coinciden entonces es un pais repetido
                    # si es falso mejor_coincidencia queda con el valor pais asignado al comienzo
                    mejor_coincidencia=p
                    valida=True
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
    return mejor_coincidencia,valida
