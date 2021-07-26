def calculadora(num1, num2):
    operacao = input("Digite o sinal da operação desejada ( +  -  *  /  ): " )

    if operacao == "+":
        return num1 + num2

    elif operacao == "-":
        return num1 - num2

    elif operacao == "*":
        return num1 * num2

    elif operacao == "/":
        return num1 / num2

    else:
        return "NÃO ENTENDI !!!"

print(calculadora(float(input("Digite um número: ")), float(input("Digite um número: "))))