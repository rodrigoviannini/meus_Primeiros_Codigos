"Faça um script que leia dois números e informe o maior deles."

primeiroNum = int(input("Digite um número inteiro: "))
segundoNum = int(input("Digite um número inteiro: "))

if primeiroNum > segundoNum:
    print(f"\nO maior número é o primeiro: {primeiroNum}")
else:
    print(f"\nO maior número é o segundo: {segundoNum}")