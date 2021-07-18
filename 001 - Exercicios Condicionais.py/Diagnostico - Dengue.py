"""Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, 
tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:

a. Sente dor no corpo?

b. Você tem febre?

c. Você tem tosse?

d. Está com congestão nasal?

e. Tem manchas pelo corpo?

Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças

"""

# DIAGNÓSTICOS - WHILE AND FOR

listaDePerguntas = ["a. Sente dor no corpo?",
                    "b. Você tem febre?",
                    "c. Você tem tosse?",
                    "d. Está com congestão nasal?",
                    "e. Tem manchas pelo corpo?"]

listaRespostas = [] # lista vazia, pq nao tenho resposta no inicio

# Para cada elemento eu faço uma pergunta

# PARA CADA ELEMENTO FAÇO UMA PERGUNTA, ASSIM:

for perguntas in listaDePerguntas:
    print(perguntas)
    respostas = input("'S' ou 'N': ").upper()
    
    while respostas not in ['S', 'N']: # Enquanto resposta nao estiver dentro das minhas opções
        respostas = input("Resposta inválida! \nDigite 'S' ou 'N': ").upper()
        
    listaRespostas.append(respostas)       

# CRIANDO A LISTA DE DIAGNÓSTICO, PORTANTO:

dengue = list("SSNNS")
gripe = [list("SSSSN"), list("SSNNS")]
semDoencas = [list("SNNNN"), list("NNNNN")]

# CRIANDO AS CONDICIONAIS E GERANDO OUTPUTS, DESTA FORMA:

if listaRespostas == dengue:
    print("Suspeita de dengue!")
elif listaRespostas in gripe:
    print("Suspeita de gripe!")
elif listaRespostas in semDoencas:
    print("Sem suspeitas!")
else:
    print("Consulte um médico!")


