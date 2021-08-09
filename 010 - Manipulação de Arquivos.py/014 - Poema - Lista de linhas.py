f = open("poema.txt", "r", encoding="utf-8")

lista_de_linhas = []

# aqui, o python entende que ele deve percorrer cada linha do arquivo!
for elemento in f:
    
    lista_de_linhas.append(elemento)
    
f.close()
print()
print(lista_de_linhas)
print()