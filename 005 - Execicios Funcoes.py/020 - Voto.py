"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONALou OBRIGATÓRIO nas eleições
"""

def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16:
    return f'Com {idade} anos: NÃO VOTA'
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos: VOTO OPCIONAL'
  else:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO'
# PROGRAMA PRINCIPAL
nasc = int(input("Qual ano voce nasceu? "))
print(voto(nasc))

print()

print(voto(2000))
print(voto(1950))
print(voto(2004))
print(voto(2011))