# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o ROJO

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from unittest import result


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

NumCheck=False
Resultado=0
var=3

while not NumCheck:
  try:
    print('Ingrese Numero 1:')
    Numbero_1=float(input())
    print('Ingrese Numero 2:')
    Numbero_2=float(input())
    
  
    if isinstance(Numbero_1, float) and isinstance(Numbero_2, float):
      NumCheck=True
    OpCheck=False
    while OpCheck==False:
      print("Que operacion desea realizar?\n+= Suma\n-= Resta\n*= Multiplicación\n/= División\n**= Exponente/Potencia)")
      Operador=input()
      if  Operador == "+":
        Resultado=Numbero_1+Numbero_2
        OpCheck=True
      elif Operador == "-":
        Resultado=Numbero_1-Numbero_2
        OpCheck=True
      elif Operador == "/":
        Resultado=Numbero_1/Numbero_2
        OpCheck=True
      elif Operador == "*":
        Resultado=Numbero_1*Numbero_2
        OpCheck=True
      elif Operador == "**":
        Resultado=Numbero_1**Numbero_2
        OpCheck=True
      else:
        print("El operador ingresado es incorecto")
        OpCheck=False
      
  except ValueError:
      print('#Error: Caracter no es valido. Ingrese Numero')
print("El resultado de la operacion {} {} {}= {}".format(Numbero_1,Operador, Numbero_2,Resultado))

