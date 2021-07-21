lista = [4, 5, 6, 5, 56, 7, -10, 78, 80, 9]

for elemento in lista:
    
    if elemento < 0:
        # quebrando o laço ao encontrar um elemento negativo
        continue
    
    print(elemento)