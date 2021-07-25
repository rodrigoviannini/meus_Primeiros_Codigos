num = int(input("Digite um número: "))
listaFatorial = list(range(1, num + 1))
fatorial = 1
print(listaFatorial)

for elemento in listaFatorial:
    fatorial *= elemento

print(f"O fatorial de {num} é {fatorial}")
print("Fim do programa!")