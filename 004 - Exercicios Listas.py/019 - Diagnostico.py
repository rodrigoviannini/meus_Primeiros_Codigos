lista_de_perguntas = ["a. Sente dor no corpo?",
                      "b. Você tem febre?",
                      "c. Você tem tosse?",
                      "d. Está com congestão nasal?",
                      "e. Tem manchas pelo corpo?"]

lista_de_respostas = []

for pergunta in lista_de_perguntas:
    
    resposta = input(pergunta + " (Digite s ou n) ")
    
    while resposta not in ["s", "n"]: 
        
        resposta = input("Não entendi!\n" + pergunta + " (Digite s ou n) ")
        
    lista_de_respostas.append(resposta)
    
# criando as listas de diagnostico
dengue = list("ssnns")
gripe = [list("ssssn"), list("ssnns")]
sem_doencas = [list("snnnn"), list("nnnnn")]

if lista_de_respostas == dengue:
    
    print("\nPaciente com dengue!")
     
elif lista_de_respostas in gripe:

    print("\nPaciente com gripe!")
    
elif lista_de_respostas in sem_doencas:
    
    print("\nPaciente sem doença aparente!")

else:
    
    print("\nProcure um Médico!!")
