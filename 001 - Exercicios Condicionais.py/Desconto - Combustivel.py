"""Um posto está vendendo combustíveis com as seguintes tabelas de desconto:

Alcool: 
até 20 lts -> 3% desconto/ litro
acima de 20 lts -> 5% desconto/ litro

Gasolina: 
até 20 lts -> 4% desconto/ litro
acima de 20 lts -> 6% desconto/ litro

Escreva um algoritmo que leia o numero de litros vendidos, o tipo de combustivel (codificado da seguinte forma: A - alcool, G - gasolina), 

Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é de 2,50 reais e o pkreço do litro do alcool é de 1,90 reais

"""

litros = int(input("Quantos litros: "))
tipoCombustivel = input("Qual combustível: (A/G): ").upper()

precoG = 2.5
precoA = 1.9
valorTotal = None # mesma coisa que -> valorTotal = 0

if tipoCombustivel == "A":
  if litros <= 20:
    valorTotal = litros * precoA * 0.97 # 3%
  else:
    valorTotal = litros * precoA * 0.95 # 5%


else:
  if litros <= 20:
    valorTotal = litros * precoG * 0.96 # 4%
  else:
    valorTotal = litros * precoG * 0.94 # 6%

print("O valor total a ser pago é de: ", valorTotal, "reais")