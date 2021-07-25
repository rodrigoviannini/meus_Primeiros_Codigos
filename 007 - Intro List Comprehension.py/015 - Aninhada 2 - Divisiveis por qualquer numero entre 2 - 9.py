listaDivi_Nove = [numeros for numeros in range(1, 1001) if True in [numeros % divisor == 0 for divisor in range(2,10)]]
print(listaDivi_Nove)