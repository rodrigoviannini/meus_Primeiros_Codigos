"Faça um script que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0."

numero = 0 
numero = float(input("digite um número:[0 para parar!]")) # Permite digitar fora do WHILE

while numero != 0: # flag
    numero += 1
    numero = float(input("digite um número:[0 para parar!]")) # Adcionando um novo input idêntico, meu contador não cria uma sequência
    print(numero)
    
print("Fim")