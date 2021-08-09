f = open("poema.txt", "r", encoding="utf-8")

for linha in f:
    print(linha)

f.close()
