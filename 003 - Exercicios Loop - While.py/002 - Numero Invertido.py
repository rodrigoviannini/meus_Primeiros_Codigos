""" Reverse a given intereger number"""

numero = int(input("Digite um numero: "))
numeroInvertido = 0 

while numero > 0:
    unidade = numero % 10 # Se numero = 1234, com % 10 -> pego a unidade 4!
    # print("Unidade: ", unidade)
    numero //= 10
    numeroInvertido *= 10
    numeroInvertido += unidade


print("Número invertido: ", numeroInvertido)
