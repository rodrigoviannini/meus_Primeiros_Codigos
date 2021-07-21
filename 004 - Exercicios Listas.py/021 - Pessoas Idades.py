'''Faça um programa que leia nome e idade de 5 pessoas e 
coloque os nomes em uma lista e as idades em outra.
Apresente as duas listas preenchidas.'''

pessoas = []
idades = []

for c in range(0,2):
    pessoas.append(input('Digite o nome da pessoa: '))
    idades.append(int(input('Digite agora a idade da pessoa: ')))
    
print(f" Os nomes listados são: {pessoas}")
print(f" As idades das pessoas são, respectivamente: {idades}")