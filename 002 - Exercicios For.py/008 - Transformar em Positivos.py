lista = [4, 5, -7, 2, 14, -45, 67, -8, 8, -9, 0, 12]
listaPositivos = []

for elemento in lista:
    if elemento < 0:
        listaPositivos.append(elemento * -1)
    else:
        listaPositivos.append(elemento)

#print("Elementos transformados em POSITIVOS: ", listaPositivos)
print("Todos os elementod da lista agora são POSITIVOS: ", listaPositivos)