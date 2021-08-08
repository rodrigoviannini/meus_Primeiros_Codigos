# modo r para a leitura, apenas
arquivo = open('ola.txt', 'r', encoding="utf-8")

conteudo = arquivo.read() #ler

arquivo.close()

print(conteudo)