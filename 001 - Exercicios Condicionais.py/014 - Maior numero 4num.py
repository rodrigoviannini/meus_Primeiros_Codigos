"""Faça o mesmo programa do exercício anterior, porém com 4 números."""

num1 = float(input("Digite um n°: "))
num2 = float(input("Digite um n°: "))
num3 = float(input("Digite um n°: "))
num4 = float(input("Digite um n°: "))

if num2 < num1 > num3 and num1 > num4:
  print("O maior número é o primeiro digitado = ", num1)

elif num1 < num2 > num3 and num2 > num4:
  print("O maior número é o segundo digitado = ", num2)

elif num1 < num3 > num2 and num3 > num4:
  print("O maior número é o terceiro digitado = ", num3)
  
elif num1 < num4 > num2 and num4 > num3:
  print("O maior número é o quarto digitado = ", num4)

else:
  print("Os números não se diferem!")