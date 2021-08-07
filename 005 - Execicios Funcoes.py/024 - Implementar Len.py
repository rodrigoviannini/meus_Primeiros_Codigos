# Como podemos implementar a função LEN()

def lenght(string):
  tamanho = 0
  for letra in string:
    tamanho += 1
  return tamanho # Esperar interar com toda a string

lenght('Essa turma tá que tá!')