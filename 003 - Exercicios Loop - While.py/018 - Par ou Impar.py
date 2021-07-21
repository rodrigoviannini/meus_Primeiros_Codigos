# Exemplo de WHILE par e ímpar.

num = 1
par = 0
impar = 0

while num != 0:
    num = int(input("Digite um número: "))
    if num == 0:
        print("número neutro!")
    elif num %2 == 0:
        print("número par")
    else:
        print("número ímpar")