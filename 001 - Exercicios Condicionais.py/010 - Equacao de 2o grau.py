# IF -> CALCULE UMA EQUAÇÃO DE 2º GRAU

a = float(input("Digite o valor de a: ")) #CASO 1 -> não é uma equação do 2o grau

if a == 0:
    print("O valor de a não pode ser ZERO!!!")
    
else: # CASO 2 -> é uma equação do 2o grau
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))


    delta = (b**2) - (4 * a * c)
    print(f"O valor de delta é: {delta}")

    if delta < 0:
        print("Raízes complexas, não tem como calcular")
    
    elif delta == 0:
        x = -b/(2*a)
        print(f"Raiz única, x = {x}")

    else:
        x1 = (-b + delta**(1/2)) / (2 * a)
        x2 = (-b - delta**(1/2)) / (2 * a)
        print(f"Raizes de x1 = {x1} e x2 = {x2}")