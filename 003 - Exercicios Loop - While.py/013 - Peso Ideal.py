sexo = str(input("Digite o seu sexo aqui: "))
altura = float(input("Digite sua altura em metros: "))


while ((sexo != 'feminino') and (sexo != 'masculino')):
    sexo = input("Digite o seu sexo aqui: ")
if sexo == ('feminino'):
    peso_ideal = (62.1 * altura) - 44.7
elif sexo == ('masculino'):
    peso_ideal = (72.7 * altura) - 58
else:
    print("Digite feminino ou masculino")
        
print(f"O peso ideal para o sexo {sexo}, na  altura de {altura} é : {peso_ideal}!")
