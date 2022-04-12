def lista_aleatoria (inicio, fin, cantidad):
    lista_val=[]
    for i in range(cantidad):
        numero=random.randrange(inicio,fin+1)
        lista_val.append(numero)
    return lista_val

# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar

def contar (lista,numero):
    return lista.count(numero)
    
# --------------------------------

if __name__ == '__main__':

    cantidad_jugadores=0

    print("Bienvenidos al Juego de GENERALA")
    Respuesta=str.upper(input("Sabes jugar a la Generala: SI/NO\n"))
    
    if Respuesta=="SI":
        print("Primero tenemos que definir la cantidad de jugadores")
        try:
            cantidad_jugadores=int(input("Cual es la cantidad de jugadores\n"))
            
        except ValueError:
            print('#Error: Caracter no es valido. ingrese nuevamente')
