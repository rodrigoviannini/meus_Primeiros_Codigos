lista = [4, 5, -7, 2, 14, -45, 67, -8, 8, -9, 0, 12]

listaPositivos = []
listaNegativos = []

for numeros in lista:
    if numeros >= 0:
        listaPositivos.append(numeros)
        
    else:
        listaNegativos.append(numeros)

print(listaPositivos)
print(listaNegativos)