# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio


CheckValue=True
while CheckValue:
    try:
        Palabra_1 = str(input('Ingrese la primera palabra:\n'))
        Palabra_2 = str(input('Ingrese la segunda palabra:\n'))
        Palabra_3 = str(input('Ingrese la tercera palabra:\n'))
        CheckValue=False
    except ValueError:
        print("Error: algo salio mal vuelva a intentarlo")


Respuesta = int(input('Ingrese el:\n 1)Ordenar las 3 palabras por orden alfabético \n 2)Ordenar las 3 palabras por cantidad de letras\n Resupesta='))
if Respuesta==1:
    if Palabra_1 > Palabra_2 and Palabra_1 > Palabra_3:
        if Palabra_2 > Palabra_3:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 2 ={}\n 3ra: Palabra 3 ={}".format(Palabra_1,Palabra_2,Palabra_3))
        elif Palabra_3 > Palabra_2:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 3 ={}\n 3ra: Palabra 2 ={}".format(Palabra_1,Palabra_3,Palabra_2))
        elif Palabra_2==Palabra_3:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 2 y  Palabra 3 ={}".format(Palabra_1,Palabra_2))
        else:
            print("Error: Algo salio mal")
    elif Palabra_2 > Palabra_1 and Palabra_2 > Palabra_3:
        if Palabra_1 > Palabra_3:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 1 ={}\n 3ra: Palabra 3 ={}".format(Palabra_2,Palabra_1,Palabra_3))
        elif Palabra_3 > Palabra_1:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 3 ={}\n 3ra: Palabra 1 ={}".format(Palabra_2,Palabra_3,Palabra_1))
        elif Palabra_1==Palabra_3:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 1 y  Palabra 3 ={}".format(Palabra_2,Palabra_1))
        else:
            print("Error: Algo salio mal")
    elif Palabra_3 > Palabra_2 and Palabra_3 > Palabra_1:
        if Palabra_1 > Palabra_3:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 1 ={}\n 3ra: Palabra 3 ={}".format(Palabra_3,Palabra_1,Palabra_2))
        elif Palabra_2 > Palabra_1:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 2 ={}\n 3ra: Palabra 1 ={}".format(Palabra_3,Palabra_2,Palabra_1))
        elif Palabra_1==Palabra_2:
            print("El orden alfabético de Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 1 y  Palabra 1 ={}".format(Palabra_3,Palabra_1))
        else:
            print("Error: Algo salio mal")
    elif Palabra_1==Palabra_2==Palabra_3:
        print("Todas las palabras son iguales a:{}".format(Palabra_1))
    else:
        print("Error: Algo salio mal")
    "================================================================================================================================================"
    "========================================================RESPUESTA 2============================================================================="
    "================================================================================================================================================"        
elif Respuesta==2:
    if len(Palabra_1) > len(Palabra_2) and len(Palabra_1) > len(Palabra_3):
        if len(Palabra_2) > len(Palabra_3):
            print("El orden por cantidad de letras de Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 2 ={}\n 3ra: Palabra 3 ={}".format(len(Palabra_1),len(Palabra_2),len(Palabra_3)))
        elif len(Palabra_3) > len(Palabra_2):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 3 ={}\n 3ra: Palabra 2 ={}".format(len(Palabra_1),len(Palabra_3),len(Palabra_2)))
        elif len(Palabra_2)==len(Palabra_3):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 1 ={}\n 2da: Palabra 2 y  Palabra 3 ={}".format(len(Palabra_1),len(Palabra_2)))
        else:
            print("Error: Algo salio mal")
    elif len(Palabra_2) > len(Palabra_1) and len(Palabra_2) > len(Palabra_3):
        if len(Palabra_1) > len(Palabra_3):
            print("El orden por cantidad de letras de Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 1 ={}\n 3ra: Palabra 3 ={}".format(len(Palabra_2),len(Palabra_1),len(Palabra_3)))
        elif len(Palabra_3) > len(Palabra_1):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 3 ={}\n 3ra: Palabra 1 ={}".format(len(Palabra_2),len(Palabra_3),len(Palabra_1)))
        elif len(Palabra_1)==len(Palabra_3):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 2 ={}\n 2da: Palabra 1 y  Palabra 3 ={}".format(len(Palabra_2),len(Palabra_1)))
        else:
            print("Error: Algo salio mal")
    elif len(Palabra_3) > len(Palabra_2) and len(Palabra_3) > len(Palabra_1):
        if len(Palabra_1) > len(Palabra_3):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 1 ={}\n 3ra: Palabra 3 ={}".format(len(Palabra_3),len(Palabra_1),len(Palabra_2)))
        elif len(Palabra_2) > len(Palabra_1):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 2 ={}\n 3ra: Palabra 1 ={}".format(len(Palabra_3),len(Palabra_2),len(Palabra_1)))
        elif len(Palabra_1)==len(Palabra_2):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 3 ={}\n 2da: Palabra 1 y  Palabra 2 ={}".format(len(Palabra_3),len(Palabra_1)))
        else:
            print("Error: Algo salio mal")
    elif len(Palabra_1)==len(Palabra_2) and len(Palabra_1) != len(Palabra_3) :
        if len(Palabra_1) > len(Palabra_3):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra: Palabra 1 y  Palabra 2 ={}\n 2da: Palabra 3 ={}".format(len(Palabra_1),len(Palabra_3)))
        elif len(Palabra_1) < len(Palabra_3):
            print("El orden por cantidad de letras Mayor a menor es de: \n 1ra:  ={}\n 2da: Palabra 1 y  Palabra 2 Palabra 3 ={}".format(len(Palabra_1),len(Palabra_3)))
        else:
             print("Error: Algo salio mal")                   
        print("Todas las palabras tienen igual cantidad de :{} caracteres".format(len(Palabra_1)))
    elif len(Palabra_1)==len(Palabra_2)==len(Palabra_3):
        print("Todas las palabras tienen igual cantidad de :{} caracteres".format(len(Palabra_1)))
    else:
        print("Error: Algo salio mal")

else:
    print("Error: Respuesta incorecta")


print("\n====================================================="  
      "\n====================================================="
      "\n==PROGRAMA FINALIZO. MUCHAS GRACIAS. VUELVA PRONTO==="
      "\n====================================================="
      "\n=====================================================")
