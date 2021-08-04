def fatorial(num = 1): 

  '''Função Fatorial,
      i: Garanto que meu início comece com valor 1,
      f: indo até 0,
      p: andando de -1 em -1, o que caracteriza o fatorial
  '''
  
  f = 1 # f recebe 1
  for c in range(num, 0, -1): # c = contador, vai receber n, jogar em num, vir de -1 em -1 ate zero
    f *= c # f = f * n, 1 * 4 = 4, retorna 4, depois com 3, 2 e 1, no fim soma tudo!
  return f

# PROGRAMA PRINCIPAL
n =int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}') 