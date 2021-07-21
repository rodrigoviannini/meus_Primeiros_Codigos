'''Faça um script que reproduza o padrão usando "*" 
a seguir de acordo com o número de linhas desejadas pelo usuário. 
Dica: print(5 * '@')'''


caract = '@'
qtde = int(input("Digite a quantidade a repetir: "))
qtde_C = (caract)

cont = 0

for c in range(0, qtde):
    cont += 1
    print(cont * qtde_C)
  
