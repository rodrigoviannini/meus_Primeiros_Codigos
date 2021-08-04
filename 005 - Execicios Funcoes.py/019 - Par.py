# PAR

def par(n=0):
  if n % 2 == 0:
    return True
  else:
    return False

num = int(input('Digite um número: '))
print(par(num)) # devolve um boolean

if par(num):
  print('Par')
else:
  print('Ímpar')