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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


CheckValue=True
while CheckValue:
    try:
        numero_1 = int(input('Ingrese el primer número:\n'))
        numero_2 = int(input('Ingrese el segundo número:\n'))
        CheckValue=False
    except ValueError:
        print("Error: algo salio mal vuelva a intentarlo") 

Resultado=numero_1-numero_2

print("La resta de {} y {} es {}".format(numero_1,numero_2,Resultado))

if Resultado == 0:
    print("Numero 1 es Igual a 0 => {} = 0".format(Resultado))
elif  Resultado < 0:
    print("Numero 1: {} es es NEGATIVO ".format(Resultado))
elif  Resultado > 0:
    print("Numero 1:{} es POSITIVO".format(Resultado))
else:
    print("Error: algo salio mal vuelva a intentarlo")