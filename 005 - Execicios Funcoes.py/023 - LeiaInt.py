"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(msg): # msg = ('Digite um n: '))
  ok = False
  valor = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print()
      print('=' *35)
      print('\nERROOO!!! Digite um número válido: \n')
      print('=' *35)
      print()
    if ok:
      break
  return valor

# PROGRAMA PRINCIPAL

n = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o número {n}')