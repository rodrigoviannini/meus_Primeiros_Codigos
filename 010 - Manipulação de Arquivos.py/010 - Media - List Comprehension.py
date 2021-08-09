arquivoNotas = open("notas.txt", "r", encoding="UTF-8")

strNotas = arquivoNotas.read()

listaNotasInteiros = [int(notas) for notas in strNotas.strip().split("\n")]
#listaNotasInteiros

media = sum(listaNotasInteiros)/len(listaNotasInteiros)
print(media)

arquivoNotas = open("notas.txt", "r", encoding="UTF-8")

strNotas = arquivoNotas.read()

listaNotasInteiros = [int(notas) for notas in strNotas.strip().split("\n")]
#listaNotasInteiros

media = sum(listaNotasInteiros)/len(listaNotasInteiros)
print(media)

arquivoNotas.close()