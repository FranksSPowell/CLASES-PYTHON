#Como generar un diccionario


mi_diccionario={"nombre":"Max","Apellido":"Power", "DNI":11111111}


for k, v in mi_diccionario.items():
    print("---------")
    print("Clave", k)
    print("Valor", v)

print("----------------------------------------------------------------------------")
for k in mi_diccionario.items():
    print("---------")
    print("Clave", k)
    
print("----------------------------------------------------------------------------\n\n")
print(mi_diccionario)


mi_diccionario["nombre"]="Maxuel"

print(mi_diccionario)

mi_lista_diccionarios=[]

mi_diccionario1={"nombre":"Juan","Apellido":"Perez", "DNI":22222222}


mi_lista_diccionarios.append(mi_diccionario)
mi_lista_diccionarios.append(mi_diccionario1)

print("----------------------------------------------------------------------------\n\n")
print(mi_lista_diccionarios[0]["nombre","Apellido"])
print(mi_lista_diccionarios[1]["nombre","Apellido"])
