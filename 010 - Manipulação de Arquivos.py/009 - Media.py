arquivoNotas = open("notas.txt", "r", encoding="UTF-8")

strNotas = arquivoNotas.read()

listaDeNotas = strNotas.strip().split("\n") 
listaDeNotasInteiro = []
for notas in listaDeNotas: # 2º elemento de List Comprehension
    listaDeNotasInteiro.append(int(notas)) # 1º elemento de List Comprehension (.append)
    
media = sum(listaDeNotasInteiro)/len(listaDeNotasInteiro)
print(media)

arquivoNotas.close()