# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio

from typing import get_type_hints
Var_Nombre: str
Var_DNI=0
Var_edad=-1
Var_altura=0.0
VarError=True

while VarError==True:
  try:
    Var_Nombre =str(input("Ingrese su nombre y apellido "))
    while not int(Var_DNI) in range(1111111,999999999):
      Var_DNI    =int(input("Ingrese su DNI (sin puntos) "))
    while not int(Var_edad) in range(0,150):
      Var_edad   =int(input("Ingrese su edad "))
    while not float(Var_altura) !=0:
      Var_altura =float(input("Ingrese altura en Metros separados por un Punto(.) "))
    VarError=False
  except ValueError:
    print('#Error: Caracter no es valido. ingrese nuevamente')

print("Nombre Completo: {} , DNI:{}\n".format(Var_Nombre,Var_DNI))

print("Nombre completo: {}\nedad:{}\naltura:{}".format(Var_Nombre,Var_edad,Var_altura))