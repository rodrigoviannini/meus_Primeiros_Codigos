'''Faça um programa que peça 10 números para o usuário e guarde os números em uma lista.
Imprima os itens da lista preenchida de trás para frente.'''

cont = 0

lista_Numeros = []

qtde_Numeros = 10

numeros = float(input(f"Digite {qtde_Numeros} números: "))


while cont < qtde_Numeros:
    
    lista_Numeros.append(numeros)
    cont += 1
    numeros = float(input(f"Digite {qtde_Numeros} números: "))
    
print(f"\nNúmeros armazenados na lista em ordem de inclusão:{lista_Numeros}")

print(f"\nNúmeros armazenados na lista em ordem decrescente: {sorted(lista_Numeros, reverse = True)}")

