"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(jog = '<desconhecido>', gol=0):
  print(f'O jogador {jog} fez {gol} gol(s)')



# PROGRAMA PRINCIPAL
n = str(input('Nome do Jogador: ')).title()
g = str(input('Número de gols: '))

# Pseudo-tratamento de (g)

if g.isnumeric(): # Se número de gols for um número, então g recebe um inteiro(g)
  g = int(g)
else:
  g = 0 # Se número de gols não for um número, então g recebe zero

# Pseudo-tratamento de (n)

if n.strip() == '':
  ficha(gol=g)
else:
  ficha(n, g)
