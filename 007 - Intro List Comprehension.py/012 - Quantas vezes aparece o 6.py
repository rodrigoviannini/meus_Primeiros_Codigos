listaNumerosSeis = [(list(str(numeros)).count("6")) for numeros in range(1, 1001)]
print(sum(listaNumerosSeis))