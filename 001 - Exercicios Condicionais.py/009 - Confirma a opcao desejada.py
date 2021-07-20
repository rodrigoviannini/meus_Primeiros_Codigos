'Faça um script de menu que mostra na tela, com o título de "Menu Principal" e mais três opções:'

# 1. FIM
# 2. CADASTRO
# 3. CONSULTA

"O programa recebe um input do teclado a opção desejada e mostra uma mensagem confirmando a opção escolhida."
# Caso a opção escolhida seja inválida, mostrar uma mensagem de erro "Opção Inválida"."

print("-=-=- MENU PRINCIPAL -=-=-")
print("\nDigite a opção desejada para prosseguir:\n")

print("Digite 1 -> FIM")
print("Digite 2 -> CADASTRO")
print("Digite 3 -> CONSULTA")

fim = "FIM"
cadastro = "CADASTRO"
consulta = "CONSULTA"

option = int(input("\nDigite a opção desejada: "))

if option == 1:
    print(f"\nOpção 1: {fim}")
elif option == 2:
    print(f"\nOpção 2: {cadastro}")
elif option == 3:
    print(f"\nOpção 3: {consulta}")
        
else:
    print("Opção Inválida")
    