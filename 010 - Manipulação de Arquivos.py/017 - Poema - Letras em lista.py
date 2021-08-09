f = open("poema.txt", "r", encoding="utf-8")

frase = f.readline() # Cada linha é uma frase

lista = [letra for palavra in frase.split() for letra in palavra] # palavra para cada palavra dentro de frase, separo pelo espaço

f.close()

print(lista)

"""DESTRINCHANDO O LIST COMPREHENSION

lista = []
2   for palavra in frase.split():
3       for letra in palavra:
1           lista.append(letra) 

"""