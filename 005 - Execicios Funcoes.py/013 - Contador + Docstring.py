def contador(i,f,p): # inicio, fim e passo
  c = i
  while c <= f:
    print(f'{c}', end=' ')
    c += p
  print('FIM!')

contador(0,100,10)