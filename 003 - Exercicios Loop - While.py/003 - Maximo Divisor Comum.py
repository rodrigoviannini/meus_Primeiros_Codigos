""" Escreva um programa que encontra o máximo divisor comum entre dois números"""

numA = int(input("Digite um número: "))
numB = int(input("Digite um número: "))

mdc = 1 # Divisão entre dois inteiros sempre é 1

# Preciso achar o maior numero e guardá-lo!
# divisor -> Garantir que será divido pelo menor numero

divisor = numA 
if numB < numA: 
    divisor = numB

while divisor > 0:
    if numA % divisor == 0 and numB % divisor == 0: # Se a divisão for exata por ambos, então encontrei o meu MDC
        mdc = divisor
        break # condição atendida , então interrompo o programa
    divisor -= 1 # Se não for atingido, vou regredindo e testando

print("MDC", mdc)