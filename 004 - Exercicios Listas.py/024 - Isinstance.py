# LISTAS INTERNAS - ISINSTANCE

minhaLista = [[1, "a", 2], [3, 4, "b"], ["c", 5, "d"]]
letras = []
numeros = []

for listaInterna in minhaLista:
    for elementos in listaInterna:
        if (isinstance(elementos, str)):
            
            letras.append(elementos)
        else:
            numeros.append(elementos)
                
print(letras)
print(numeros)