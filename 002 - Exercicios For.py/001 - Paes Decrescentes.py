'''Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.'''


valor = 1
par = 0
numero = int(input("Digite um número: "))

for valor in range(numero,(-numero - 1), -1):
     if valor %2 == 0:
        par += 1
        print(f"{valor} ")