num = int(input("Digite um número: "))

fatorial = 1

for elemento in range(1, num + 1):
    fatorial *= elemento # equivalente -> fatorial = fatorial * elemento
    print(elemento, fatorial)
