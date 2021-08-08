# Modo a (APPEND), pra poder escrever ao fim do arquivo coisas novas
arquivo = open("ola.txt", "a", encoding="utf-8")

arquivo.write('\nMinha quarta frase\n') #adiciono no final do aequivo 'olá.txt'

arquivo.close()