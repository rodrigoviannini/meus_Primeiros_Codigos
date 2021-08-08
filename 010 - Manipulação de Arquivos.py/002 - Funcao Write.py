"""Uma vez aberto o arquivo, podemos escrever alguma coisa nele. Para isso, usamos a função write()

Essa função aceita apenas um argumento, que é o que vc quer escrever no arquivo"""

arquivo = open("ola.txt", "w", encoding="utf-8")
arquivo.write("olá, mundo!!!!\n")
# print(arquivo.write("olá, mundo!!!!\n"))

arquivo.close() 

"""Sempre fechar o arquivo: 
    Se alteramos o arquivo mas não o fechamos, as alterações não serão salvas.
    Se esquecermos de fechar um arquivo, outros programas podem ter problemas de acesso a ele."""