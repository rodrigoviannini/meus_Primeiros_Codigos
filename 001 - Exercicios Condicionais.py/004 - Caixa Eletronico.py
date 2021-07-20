"""Faça um progra para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão forneidas. As notas disponíveis serão de 1, 5, 10 50, 100 e 200 reais."""

valor = int(input("Quanto deseja sacar: "))

notasDuz = valor//200
valor %= 200 #valor = valor % 200

notasCem = valor//100
valor %= 100

notasCinq = valor//50
valor %= 50

notasDez = valor//10
valor %= 10

notasCinco = valor//5
valor %= 5

notasUm = valor

if notasDuz > 0:
    print(notasDuz, "notas de 200 reais")
if notasCem > 0:
    print(notasCem, "notas de 100 reais")
if notasCinq > 0:
    print(notasCinq, "notas de 50 reais")
if notasDez > 0:
    print(notasDez, "notas de 10 reais")
if notasCinco > 0:
    print(notasCinco, "notas de 5 reais")
if notasUm > 0:
    print(notasUm, "notas de 1 real")

