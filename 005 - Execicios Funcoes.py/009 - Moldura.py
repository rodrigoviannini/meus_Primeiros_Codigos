# Desenhar moldura. Construa uma função que desenhe um retângulo usando os caracteres "+" "-" "|"
# Esta função deverá receber dois parâmetros -> Linhas e Colunas

"""
-------
| | | |
|-+-+-|
| | | |
|-+-+-|
| | | |
-------

"""
def montaLinha(c):
    return "-" + "--" * c

def montaLinhaPipe(c):
    return "|" + " |" * c

def montalinhaDivisoria(c):
    return "|" + "-+" * (c-1) + "-|"

def montaMatriz(l, c):
    linha = montaLinha(c)
    linhaPi = montaLinhaPipe(c)
    linhaDiv = montalinhaDivisoria(c)
    print()
    print(linha)

    for i in range(0, l-1):
        
        print(linhaPi)
        print(linhaDiv)
    print(linhaPi)
    print(linha)
    print()

linhas = int(input("Quantas linhas você deseja: "))
colunas = int(input("Quantas colunas você deseja: "))
montaMatriz(linhas, colunas)
