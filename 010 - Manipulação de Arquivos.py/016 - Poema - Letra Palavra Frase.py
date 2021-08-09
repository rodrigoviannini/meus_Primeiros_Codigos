f = open("poema.txt", "r", encoding="utf-8")

for linha in f:
    listaFrase = linha.split()
    #print(list(listaFrase)) 

    """Para imprimir listaFrase, deve-se comentar o p´roximo bloco de Loop For"""
    
    for palavra in listaFrase:
        print(palavra)
        #print(list(palavra))          
        
f.close()