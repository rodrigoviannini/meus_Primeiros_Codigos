def calculadora(num1, num2):

    operacao = input("Digite o sinal da operação desejada ( +  -  *  /  ): " )

    while operacao not in ["+", "-", "*", "/"]:
        operacao = input("\n\n-=-=-=-=- Operação Inválida!!! -=-=-=-=-  \n\nDigite a operação desejada ( +  -  *  /  ): " )
    if operacao == "+":
        return num1 + num2

    elif operacao == "-":
        return num1 - num2

    elif operacao == "*":
        return num1 * num2

    elif operacao == "/":
        return num1 / num2

print(calculadora(float(input("Digite um número: ")), float(input("Digite um número: "))))