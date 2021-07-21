divisor = 1
contador = 0

numero = int(input("Digite um número inteiro: ")) # digitar um numero inteiro qualquer

while divisor <= numero: # Enquanto meu divisor for menor que meu input
    if numero % divisor == 0: #Verifica se o resto da divisão é ZERO, se for é divisor
        print(divisor)
        contador += 1
    
    divisor += 1 # Contador é igual a contador mais um
print(f"Qtde de Divisores {contador} divisor(es)")