"""Faça um programa que leia 3 números e informe o maior deles."""

num1 = float(input("Digite um n°: "))
num2 = float(input("Digite um n°: "))
num3 = float(input("Digite um n°: "))

if num2 < num1 > num3:
  print("O maior número é o primeiro digitado = ", num1)

elif num1 < num2 > num3:
  print("O maior número é o segundo digitado = ", num2)

else:
  print("O maior número é o terceiro digitado = ", num3)