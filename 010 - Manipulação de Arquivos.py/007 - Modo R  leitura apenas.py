# modo r para a leitura, apenas
arquivo = open('ola.txt', 'r', encoding="utf-8")

# lê o conteúdo do arquivo
conteudo = arquivo.read()

arquivo.close()

print(conteudo)

"""A função read() lê o que estiver no arquivo em forma de uma string!"""