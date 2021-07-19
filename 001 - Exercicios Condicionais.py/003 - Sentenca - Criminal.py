"""Faça um programa que faça 5 perguntas para uma pessoa  sobre um crime> As perguntas são:

"Telefonou para a vitima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 

Se a pessoa responder positivamente a 2 questoes ela deve ser classificada como "Suspeita"
Entre 3 e 4 como "Cumplice"
Se tiver 5 respostas positivas como "Assassino"
Caso contrário, ele será classificado como "Inocente"
"""

listaPerguntas = ["Telefonou para a vitima?",
                  "Esteve no local do crime?",
                  "Mora perto da vítima?",
                  "Devia para a vítima?",
                  "Já trabalhou com a vítima?"]

listaRespostas = [] # Lista vazia pq ainda não tenho as respostas


for perguntas in listaPerguntas:
    print(perguntas)
    respostas = input("'S' ou 'N':  ").upper()

    while respostas not in ['S', 'N']:
        respostas = input("Digite uma resposta válida: 'S' ou 'N': ").upper()

    listaRespostas.append(respostas)
    

# CRIANDO A LISTA DE SENTENÇAS, PORTANTO:

suspeito = [list("SSNNN"), list("NSSNN"), list("NNSSN"), list("NNNSS")]
cumplice = [list("SSSNN"), list("NSSSN"), list("NNSSS"), list("SSSSN"), list("NSSSS")]
assassino = list("SSSSS")

# CRIANDO AS CONDICIONAIS E GERANDO OUTPUTS, DESTA FORMA:
print(listaRespostas)

if listaRespostas in suspeito:
    print("SUSPEITO")
elif listaRespostas in cumplice:
    print("CÚMPLICE")
elif listaRespostas == assassino:
    print("ASSASSINO")
else:
    print("INOCENTE")