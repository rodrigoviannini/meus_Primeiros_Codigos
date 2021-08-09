"""
O comando Write só funciona com strings, não funciona com listas, portanto, devemos tratar da seguinte forma: 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
CODIGO ORIGINAL: TypeError: write() argument must be str, not list

notas = [8, 7, 6, 10, 10, 8]

f = open("minhas_notas.txt", "w", encoding="utf-8")

f.write(notas) 

f.close()
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
A SEGUIR O TRATAMENTO:

"""

# CONVERTENDO A LISTA PARA STR ATRAVÉS DE UM LOOP FOR

notas = [8, 7, 5, 6, 4, 6]

f = open("notas.txt", "w", encoding="utf-8")

for elemento in notas:
    
    f.write(str(elemento) + "\n")
    
f.close()