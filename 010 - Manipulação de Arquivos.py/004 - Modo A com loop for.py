# modo a, pra poder escrever ao fim do arquivo coisas novas
arquivo = open("ola.txt", "a", encoding="utf-8")

for i in range(5):
    
    arquivo.write(str(i) + " - olá mundo!!\n")

arquivo.close()

arquivo