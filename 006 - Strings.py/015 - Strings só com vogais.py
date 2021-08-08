stringInicial = 'Olá Mundo'
stringFinal = '' # cria uma string vazia
for letra in stringInicial:
    if letra.lower() in 'aeiouáéíóú':
        stringFinal += letra
print(stringFinal)