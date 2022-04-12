# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

from cmath import nan


def calificar(nota):
    if nota>=90:
        return("A")
    elif nota>=80 and nota<90:
        return("B")
    elif nota>=70 and nota<80:
        return("C")
    elif nota>=60 and nota<70:
        return("D")
    elif nota<60 and nota>=0:
        return("F")
    elif nota==-1:
        return("Ausemnte")
    else:
        print("Error verifique nota")

def lenPos(lst):
    lenLst=0
    for i in lst:
        if i >=0:
            lenLst+=1
    return lenLst

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

for i in notas:
    print("La calificacion para la nota:",i, "es de :",calificar(i))

promedio_1=sum(i for i in notas if i >=0)/lenPos(notas)
print("La sumatoria de todas las notas es de: ", sum(i for i in notas if i >=0))
print("El promedio de todas las notas es de: ", sum(i for i in notas if i >=0)/lenPos(notas))

calificar(promedio_1)


print("La calificacion final es de:", calificar(promedio_1))

# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

# Imprima en pantalla al cantidad de ausentes

print("Cantidad de ausentes ", len(notas)-lenPos(notas))


print("===========================")

# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

for i in notas:
    if i> 0:sumatoria+=i
    if i> 0: cantidad_notas+=1
    if i==-1: cantidad_ausentes+=1




# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas

promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

calificacion=nan

if promedio>=90:
    calificacion=("A")
elif promedio>=80 and promedio<90:
    calificacion=("B")
elif promedio>=70 and promedio<80:
    calificacion=("C")
elif promedio>=60 and promedio<70:
    calificacion=("D")
elif promedio<60 and promedio>=0:
    calificacion=("F")
elif promedio==-1:
    calificacion=("Ausemnte")
else:
    print("Error verifique nota")


print("La sumatoria de todas las notas es de: ", sumatoria)
print("El promedio de todas las notas es de: ", sumatoria / cantidad_notas)

print("La calificacion final es de:", calificacion)

# Imprima en pantalla al cantidad de ausentes

print("La cantidad de ausentes es de :", cantidad_ausentes)