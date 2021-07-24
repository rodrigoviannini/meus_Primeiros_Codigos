provas = []
exercicios = []

# PROVAS 
cont = 0
while cont < 3:
    nota = (float(input("Digite a nota da prova " + str(cont+1) + ": "))) 
    provas.append(nota)
    cont += 1

    """Não conseguimos imprimir int com o sinal de (+), então convertemos para string | cont + 1 -> pq iniciamos o contador em zero, senão retornaria prova 0!"""

# EXERCICIOS   
cont = 0
while cont < 4:
    nota = (float(input("Digite a nota da exercício " + str(cont+1) + ": ")))
    exercicios.append(nota)
    cont += 1

#CÁLCULOS PONDERADOS
mP = (provas[0] + 2*provas[1] + 2*provas[2]) / 5
mE = (exercicios[0] + exercicios[1] + 2*exercicios[2] + 3*exercicios[3]) / 7

# CONDICIONAIS E MÉDIA FINAL
if mP >= 5 and mE >=5:
    media_Final = (2*mP + mE) / 3
else: 
    media_Final = min(mP, mE)
print("Média final: ", round(media_Final,2))

"""DESAFIO -> ADAPTAR ESSE PROGRAMA PARA VÁRIOS ALUNOS"""