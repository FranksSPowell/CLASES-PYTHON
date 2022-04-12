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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

def Average(lst):
    return sum(lst) / len(lst)

ListaDeNumeros=[]
CheckValue=True
respuesta=""
while CheckValue:
    try:
        print("Ingrese las temperaturas en grados centigrados")
        Cantidad= int(input('Ingrese el cantidad de temperaturas que quiere ingresar:\n'))
        for x in range(0,Cantidad):
            ListaDeNumeros.append(int(input('Ingrese la temperatura N° {} :\n'.format(len(ListaDeNumeros)+1))))
        respuesta=str(input("Desea agregar mas temeraturas? SI/NO:\n"))
        if str.upper(respuesta)=="SI":
            CheckValue=True
        elif str.upper(respuesta)=="NO":
            print("Gracias Por ingresar las tempraturas ingresadas, sus datos seran analizados.")
            CheckValue=False
        else:
            print("Respuesta no reconozida, gracias Por ingresar las tempraturas ingresadas, sus datos seran analizados.")
            CheckValue=False
    except ValueError:
        print("Error: algo salio mal vuelva a intentarlo") 

print("La temepratura Maxima alcanzada es de {} ° ".format(max(ListaDeNumeros))) 
print("La temepratura Minima alcanzada es de {} ° ".format(min(ListaDeNumeros))) 
print("La temepratura Promedio alcanzada es de {} ° ".format(Average(ListaDeNumeros))) 
