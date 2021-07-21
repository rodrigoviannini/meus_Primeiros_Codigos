"""Imprimir estrelas em forma de losango"""

numEstrelas = int(input("Digite a qtde de estrelas desejadas: "))

contEstr = 1
esp = numEstrelas // 2

while contEstr < numEstrelas:
    print(" " * esp + "*" * contEstr)
    contEstr += 2
    esp -= 1

while contEstr >= 1:
    print(" " * esp + "*" * contEstr)
    contEstr -= 2
    esp += 1
