lista = [4, 5, 6, 5, -6, 56, 7, -10, 78, 80, 9]

lista_neg = []
lista_pos = []

for numero in lista:
    
    if numero < 0:
        lista_neg.append(numero)
    else:
        lista_pos.append(numero)
        
print(lista_pos)
print(lista_neg)
print(lista)