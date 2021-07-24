"""Dado dois vetores x e y, ambos com (n) elementos, determinar o produto escalar desses vetores

Produto escalar = [1,2] X [3,4] => 1*3 + 2*4 = 11"""

num = int(input("Digite o número de elementos: "))

vetorA = []
vetorB = []

idx = 0
while idx < num:
  vetorA.append(int(input("Digite o elemento do vetor A: " + str(idx + 1) + ": ")))
  idx += 1

idx = 0
while idx < num:
  vetorB.append(int(input("Digite o elemento do vetor B " + str(idx + 1) + ": ")))
  idx += 1

print(vetorA)
print(vetorB)

idx = len(vetorA) - 1 # retorna a qtde de elemento da lista e subtrai 1, para vir de trás para frente
produtoEscalar = 0 # variavel que soma os produtos
while idx >= 0:
  produtoEscalar += vetorA[idx] * vetorB[idx]
  idx -= 1 # estamos vindo de trás para frente   
print(produtoEscalar)
