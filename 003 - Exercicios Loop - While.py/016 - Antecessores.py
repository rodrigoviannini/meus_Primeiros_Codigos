"Faça um script que peça ao usuário para digitar um número n e some de 1 a n (some o fatorial, mas não resolva o fatorial)."

contador = 0
somar = 0

numero = int(input("Digite um número inteiro: ")) # digitar um numero inteiro qualquer

while contador < numero: # contador ele é menor que o número, para limitar meu looping
    contador += 1 
    somar += contador # Vai fazer a adição dos números impressos pelo contador
    print(contador) # Vai imprimir os numeros antecessores do input
    
else:
    print(f"\nA soma do input e seus antecessores é: {somar}.") # Vai imprimir a adição dos números