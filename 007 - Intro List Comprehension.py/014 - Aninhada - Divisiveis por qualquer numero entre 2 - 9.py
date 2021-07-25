listaDiv_Nove = [numeros for numeros in range(1, 1001) if True in [True for divisor in range(2,10) if numeros % divisor == 0]]
print(listaDiv_Nove)