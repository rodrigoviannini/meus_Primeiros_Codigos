"""É muito comum usar o for com o range para percorrer os índices de uma lista, e assim também acessar os elementos da lista através do índice.

Isso é feito passando pro range o comprinento da lista como argumento!"""

lista = ["a", "b", "c", "d", 1, 2, 5, 3]

for i in range(0, len(lista), 2):
    
    print(i, lista[i])