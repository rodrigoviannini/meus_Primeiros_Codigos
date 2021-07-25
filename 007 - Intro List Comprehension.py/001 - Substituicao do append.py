"""-> For, utilização convencional

lista = []
for x in range(5):
  lista.append(x)
print(lista)
"""

# O primeiro (x), antes do for -> equivale ao lista.append(x) da expressão acima!

lista = [x for x in range(5)] 
print(lista)
