# ESCOPO LOCAL

def teste():
  x=8
  print(f'No programa principal, n vale {n}')
  print(f'Na função teste, x vale {x}')

# PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}')
# print(f'Na função teste, x vale {x}') => NÃO FUNCIONA PQ (X) É UMA VARIÁVEL LOCAL, PORATANTO, SÓ É RECONHECIDA DENTRO DA FUNÇÃO
teste()