# usando compreensão de listas!

f = open("poema.txt", "r", encoding="utf-8")

frase = f.readline() + f.readline() + f.readline() + f.readline()

lista = [letra for letra in frase.strip().split('\n')]

print()
print(lista)
print()

f.close()