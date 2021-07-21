'''Faça um script que leia 10 números do usuário e devolva duas listas:
uma com os números ímpares e outra com os números pares.'''

lista1 = []
lista2 = []

valores = 0

'''Faça um script que leia números do usuário, enquanto ele não digitar 0.
Armazene esses números em uma lista e ao final informe quantos números foram digitados,
ignorando o 0.'''

lista = []

valores = int(input("Digite um número: "))

cont = 0

while valores != 0:
      
    #cont += 1
    lista.append(valores)
    lista.count(valores)
    valores = int(input("Digite um número: "))
    
print(f"Os valores da lista são: {lista} e foram digitados {len(lista)} números! ")