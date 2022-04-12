# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    if numero_1>numero_2:
        return numero_1
    elif numero_1<numero_2:
        return numero_2
    elif numero_1==numero_2:
        print("Los numeros son iguales")
        return numero_2
    else:
        print("Algo salio Mal")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    Numero_Mayor=imprimir_mayor(2, 10)
    print("El mayor numero es el :", Numero_Mayor)

    print("terminamos")