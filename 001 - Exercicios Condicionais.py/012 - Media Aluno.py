"""Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.

Obs.: O aluno irá passar de ano se sua média for maior que 6."""

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))

media = (nota1 + nota2 + nota3)/3

if media >=6: # Considerei a condição > ou =, levando em consideeração que se fosse apenas maior, seria aprovado com 6.1, por exemplo.
  print("Você foi aprovado!")
else:
  print("Você não foi aprovado!")