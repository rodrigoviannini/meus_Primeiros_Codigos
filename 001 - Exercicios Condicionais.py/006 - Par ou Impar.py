"Faça um script que leia dois números e informe se é Par ou Ímpar."

numero = int(input("Digite um número inteiro: "))

if numero %2 == 0:
    print(f"\n{numero} é número par")
else:
    print(f"\n{numero} é número ímpar ")