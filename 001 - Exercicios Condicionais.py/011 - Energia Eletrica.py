#Deseja-se calcular a conta de consumo de energia elétrica de um consumidor
#O preço de 1 Kwh custa atualmente R$ 0,27. O cálculo da conta é dado por:
#Preço do Kwh x Quantidade consumida Entretanto, o valor da conta não deverá ser inferior a
#R$ 13,00, ou seja, mesmo que o seu consumo seja muito baixo, ele terá que pagar
#essa taxa mínima. Elabore um Algoritmo que leia a quantidade de Kwh consumida,
#determine e exiba o total a pagar.

consumo = float(input("Digite a Qtde de Kwh consumida: "))

kwh = 0.27

total = (kwh * consumo)

if total < 13:
    print("R$" ,13, ("reais"))
else:
    print(total)