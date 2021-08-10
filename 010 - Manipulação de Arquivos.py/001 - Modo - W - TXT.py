""" FUNÇÃO OPEN():

f:  é a variável,
'olá.txt': Caminho do arquivo
'w': Modo de operação
encoding='UTF-8': codificação 'universal' do arquivo
"""

f = open("ola.txt", "w", encoding="utf-8") # CUIDADO COM O W: ele sobrescreve, ou seja, perde o que foi feito anteriormente

f.write("olá, let's code!")
print("...")

f.close()


"""MODOS: 

r - lê um arquivo existente
w - Abre um arquivo para escrita (cria caso não exista) 
a - abre um arquivo existente para adicionar informações ao seu final
x - Cria um arquivo novo
+ - ao ser combinado com outros modos, permite alteração de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)"""