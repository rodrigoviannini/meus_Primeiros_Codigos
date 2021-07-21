""" Escreva um programa que encontra o máximo divisor comum entre dois números"""

numA = int(input("Digite um número: "))
numB = int(input("Digite um número: "))

mdc = 1

# Preciso achar o maior numero e guardá-lo!
# divisor -> Garantir que divido pelo menor

divisor = numA 
if numB < numA: 
    divisor = numB

while divisor > 0:
    if numA % divisor == 0 and numB % divisor == 0:
        mdc = divisor
        break
    divisor -= 1

print("MDC", mdc)