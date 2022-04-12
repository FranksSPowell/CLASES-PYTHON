# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos



CheckValue=True
while CheckValue:
    try:
        numero_1 = int(input('Ingrese el primer número:\n'))
        numero_2 = int(input('Ingrese el segundo número:\n'))
        CheckValue=False
    except ValueError:
        print("Error: algo salio mal vuelva a intentarlo") 

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 < numero_2:
    print("Numero 2 es mayor que Numero 1 => {} > {}".format(numero_2,numero_1))
elif  numero_1 > numero_2:
    print("Numero 1 es mayor que Numero 2 => {} > {}".format(numero_1,numero_2))
elif  numero_1 == numero_2:
    print("Numero 1 es igual que Numero 2 => {} = {}".format(numero_1,numero_2))
else:
    print("Error: algo salio mal vuelva a intentarlo")
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 == 0:
    print("Numero 1 es Igual a 0 => {} = 0".format(numero_1))
elif  numero_1 % 2==0:
    print("Numero 1: {} es es par ".format(numero_1))
elif  numero_1 % 2 != 0:
    print("Numero 1:{} es impar".format(numero_1))
else:
    print("Error: algo salio mal vuelva a intentarlo")


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if numero_1 in range(0,100):
    print("El numero {} esta entre 0 y 100".format(numero_1))
else:
    print("El numero {} esta fuera del RANGO de 0 y 100".format(numero_1))

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if numero_1 <= 9 and numero_2 >=-1:
    print("El numero1: {} es menor a 10 y El numero2: {} es mayor a -2".format(numero_1, numero_2))
elif numero_1 >= 10 and numero_2 >=-1:
    print("El numero1: {} NO ES MENOR a 10 y El numero2: {} es mayor a -2".format(numero_1, numero_2))
elif numero_1 <= 9  and numero_2 <= -1:
     print("El numero1: {} es menor a 10 y El numero2: {} NO ES MAYOR a -2".format(numero_1, numero_2))
elif numero_1 >= 10  and numero_2 <= -2:
    print("El numero1: {} es NO ES MENOR a 10 y El numero2: {} NO ES MAYOR a -2".format(numero_1, numero_2))
else:
    print("Error: algo salio mal vuelva a intentarlo")