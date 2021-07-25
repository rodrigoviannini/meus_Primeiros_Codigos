"""lista = [-1, 4, 7, -3, 46, -12, 4,-9, 0]
listaPositivos = []

for num in lista:
  if num >= 0:
    listaPositivos.append(num)

print(listaPositivos)"""

lista = [-1, 4, 7, -3, 46, -12, 4,-9, 0]
listaPositivos = [num for num in lista if num >= 0 ]
print(listaPositivos)