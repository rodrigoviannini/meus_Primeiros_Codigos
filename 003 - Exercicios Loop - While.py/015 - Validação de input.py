"Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas."

# Idade: entre 0 e 150;
# Salário: maior que 0;
# Gênero: M, F ou Outro.
# Por último imprima os dados recebidos do usuário.


# IDADE
idade = int(input("\nDigite sua idade: "))

while idade > 150 or idade < 0:
    idade = int(input("\nValor inválido, digite uma idade válida "))
print(f"\nSua idade é: {idade} anos \n")

# SALÁRIO
salario = float(input("\nDigite seu salário em reais: "))

while salario < 0:
    salario = float(input("\nValor inválido, digite um valor positivo: "))
print(f"\nSeu salário é: {salario} reais \n")

#GÊNERO
genero = str(input("\nDigite M (masculino) | F (feminino) e O (outro): ")).upper()

while genero != "M" and genero != "F" and genero != "O":
    genero = str(input("\nValor inválido, digite um valor válido ")).upper()
print(f"\nSeu gênero é: {genero}  ")