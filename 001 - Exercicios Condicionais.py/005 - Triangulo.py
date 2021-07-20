""" faça um programa que peça os 3 lados de  um triângulo. O programa deverá informar se os valores podem ser um triangulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isóceles ou escaleno."""

# três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro
# Equilatero -> três lados iguais
# Isóceles -> quaisquer dois lados iguais
# Escaleno -> três lado diferentes

ladoA = int(input("Digite o valor da aresta A do triângulo:"))
ladoB = int(input("Digite o valor da aresta B do triângulo:"))
ladoC = int(input("Digite o valor da aresta C do triângulo:"))

if (ladoA + ladoB > ladoC) and (ladoB + ladoC > ladoA) and (ladoA + ladoC > ladoB):
    if ladoA == ladoB and ladoB == ladoC:
        print("É um triângulo equilátero!")
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        print("É um triângulo isóceles!")
    else: 
        print("É um triângulo escaleno!")
else:
    print("Não é um triângulo!")