f = open("poema.txt", "r", encoding="utf-8")

linhaUm = f.readline()
linhaDois = f.readline()
linhaTres = f.readline()
linhaQuatro = f.readline()

f.close()

print(linhaUm,linhaDois,linhaTres,linhaQuatro)