# FATORIAL - FOR

fatorial = 1 # Para dizer que é um inteiro e 1 não altera a multiplicação

numero = int(input("Digite um número: "))

for c in range(numero, 0, -1): # Vai do numero até xero e subtrai 1
        
    fatorial *= c # (fatorial = fatorial * c) 
    
print(fatorial)