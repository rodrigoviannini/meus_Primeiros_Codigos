nomes = ["André", "João", "Maria"]

f = open("nomes_2.txt", "w", encoding="utf-8")

for item in nomes:
    
    f.write(item)
    f.write("\n")
    
f.close()