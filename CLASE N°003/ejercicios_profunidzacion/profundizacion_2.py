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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

ListaDeNumeros={}
CheckValue=True
while CheckValue:
    try:
        ListaDeNumeros[0] = int(input('Ingrese el primer número:\n'))
        ListaDeNumeros[1] = int(input('Ingrese el segundo número:\n'))
        ListaDeNumeros[2] = int(input('Ingrese el tercer número:\n'))
        CheckValue=False
    except ValueError:
        print("Error: algo salio mal vuelva a intentarlo") 



for x in ListaDeNumeros:
    print("El Numero {} es el ={}".format(x+1,ListaDeNumeros[x]))