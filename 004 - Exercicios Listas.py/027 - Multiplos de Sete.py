"""Faça um programa que escreva todos os números multiplos de 7 entre 1 e n, sendo n um valor introduzido pelo usuário. Exemplo.: 7, 15, 21, 28, 35"""

valorIntr = int(input("Digite o valor de (n): "))
listaSete = []

cont = 7

while cont < valorIntr:
    listaSete.append(cont)
    cont += 7

print(listaSete)