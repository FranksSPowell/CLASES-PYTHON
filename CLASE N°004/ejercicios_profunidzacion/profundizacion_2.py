# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from pickle import TRUE


print("Mi Calculadora (^_^)")
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
      print("Que operacion desea realizar?\n+= Suma\n-= Resta\n*= Multiplicación\n/= División\n**= Exponente/Potencia\n o FIN: para finalizar las operaciones)")
      Operador=input()
      if  Operador == "+":
        Resultado=Numbero_1+Numbero_2
      elif Operador == "-":
        Resultado=Numbero_1-Numbero_2
 
      elif Operador == "/":
        Resultado=Numbero_1/Numbero_2

      elif Operador == "*":
        Resultado=Numbero_1*Numbero_2
     
      elif Operador == "**":
        Resultado=Numbero_1**Numbero_2
    
      elif Operador.upper() == "FIN":
        print("Gracias por sus operaciones, esperamoa haber sumado en su dia")
        break
      else:
        print("El operador ingresado es incorecto")
      #print("El resultado de la operacion {} {} {}= {}".format(Numbero_1,Operador, Numbero_2,Resultado))1
    
      print("===========================")
      print(" {}  {}  {} = {}      ".format(Numbero_1,Operador, Numbero_2,Resultado))
      print("===========================")
      print("== 7 ==== 8 ==== 9 =  +  ==")
      print("== 4 ==== 5 ==== 6 =  -  ==")
      print("== 1 ==== 2 ==== 3 =  *  ==")
      print("==============  **    /  ==")


  except ValueError:
      print('#Error: Caracter no es valido. Ingrese Numero')
