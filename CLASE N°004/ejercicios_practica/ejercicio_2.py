# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']



# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

for i in colores:
   print("El color: {}".format(i))

print("\n===========================\n")

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...

print("\n===========================\n")
for i in range(len(colores)):
    print("El color: {}".format(colores[i]))

print("terminamos!")