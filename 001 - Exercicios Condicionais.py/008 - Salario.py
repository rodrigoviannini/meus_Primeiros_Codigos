"Uma empresa irá aplicar um reajuste nos salários de seus funcionários de acordo com as seguintes regras:"

# Salário até R$2800,00 (incluindo): aumento de 20%;

# Salários entre R 2800,00 e R$7000,00: aumento de 15%;

# Salários entre R 7000,00 e R$15000,00: aumento de 10%;

# Salários de R$15000,00 em diante: aumento de 5%.

# Dado o salário de um funcionário, informe: 
    # A) o salário antes do reajuste;
    # B) o percentual de aumento aplicado;
    # C) o valor do aumento e o novo salário.
    
print("AUMENTO SALARIAL")
salarioFunc = float(input("Informe o valor do seu salário atual 'EM REAIS' para verificar o aumento obtido: "))
print(f"\nSeu salário atual é de: {salarioFunc} reais")

novoSalario_5 = salarioFunc + (salarioFunc * 0.05)
novoSalario_10 = salarioFunc + (salarioFunc * 0.10)
novoSalario_15 = salarioFunc + (salarioFunc * 0.15)
novoSalario_20 = salarioFunc + (salarioFunc * 0.20) #Incluído R$ 2800,00

if salarioFunc >= 15000:
    print(f"\nVocê irá obter um aumento salarial de 5%, seu novo salário é de: {novoSalario_5} reais")
elif 15000 > salarioFunc > 7000:
    print(f"\nVocê irá obter um aumento salarial de 10%, seu novo salário é de: {novoSalario_10} reais")
elif 7000 >= salarioFunc > 2800:
    print(f"\nVocê irá obter um aumento salarial de 15%, seu novo salário é de: {novoSalario_15} reais")
else:
    print(f"\nVocê irá obter um aumento salarial de 20%, seu novo salário é de: {novoSalario_20} reais")