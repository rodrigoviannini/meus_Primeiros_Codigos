# List comprehension -> Limitação: Não dá para Debugar!

listaGenerica = [1, 2, 3, 4, 1, 2, 3, 4, 10, 10, 10, 5, 3, -4]

listaMaior = [x for x in listaGenerica if not False in [True if x >= y else False for y in listaGenerica]]

print(listaMaior)

