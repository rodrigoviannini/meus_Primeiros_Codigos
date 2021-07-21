"""Um exemplo para o cálculo de média dos valores em uma lista, 
Mas fazemos o usuário digitar os elementos da lista, um a um!"""

cont = 0 # vou contar alguma coisa

lista_de_notas = [] # tenho uma lista vazia

quantidade = int(input("Quantas notas tem? ")) #pedir a quantidade de notas

while cont < quantidade: # enquanto o contador for menor que a qtde que o usuario me passou
    
    nota = float(input("Qual é " + str(cont+1) + "a nota? "))
    
    lista_de_notas.append(nota)
    
    cont = cont + 1 # 0 + 1 e converte para string (qual é a primeira nota?) e da um append na nota e vai colocando na lista

media = sum(lista_de_notas)/len(lista_de_notas) # media, posso usar qtde no lugar de len

print("\nA média do aluno é:", media)