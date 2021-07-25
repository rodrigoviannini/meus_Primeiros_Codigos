"""Recebo um número inteiro e imprimo a tabuada!"""

num = int(input("Digite um número: "))

if 0 < num <= 10:
    for i in range(0, 11, 1):
        print(num, "X", i, "=", num * i)

else: 
    print("Valor inválido!")
  