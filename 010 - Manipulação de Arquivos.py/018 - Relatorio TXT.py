"""A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre             456.12 MB       16.85%
2    anderson             1245.70 MB       46.02%
3    antonio               123.46 MB        4.56%
4    carlos                 91.26 MB        3.37%
5    cesar                   0.99 MB        0.04%
6    rosemary              789.46 MB       29.16%

Espaço total ocupado: 2706.98 MB
Espaço médio ocupado: 451.16 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""

# Qual o espaço ocupado pelos usuários
# Identificar os usuários com maior espaço ocupado

# Nome do usuário possui 15 caracteres
# Criar um programa que gere um relatório, chamado "relatório.txt"

def somaTudo(lista):
    soma = 0
    for colaborador in lista:
        soma += int(colaborador[1])
    return soma 

def converteByteToMegabyte(nrBytes):
    return int(nrBytes)/(2**20)

def calculaPorcentagem(lista, tamanho):
    return int(tamanho)/somaTudo(lista)*100


usuarios = open("usuarios.txt", "r", encoding="UTF-8")

listaUsuarios = [] # Precisamos de uma lista ninhada para guardar dois valores

for usuario in usuarios:
    listaUsuarios.append(usuario.split())

usuarios.close()

# CRIANDO O RELATÓRIO.TXT

relatorio = open("relatorio.txt", "w", encoding="UTF-8")

relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
relatorio.write("------------------------------------------------------------------------\n")
relatorio.write("Nr.  Usuário        Espaço utilizado     %\ do uso\n\n")


for idx, colaborador in enumerate(listaUsuarios):
    texto = f'{idx + 1}    {colaborador[0]}             {converteByteToMegabyte(colaborador[1])} MB       {calculaPorcentagem(listaUsuarios, colaborador[1])}%\n'
   
    relatorio.write(texto)


relatorio.write(f"\nEspaço total ocupado: {converteByteToMegabyte(somaTudo(listaUsuarios))} MB\n")
relatorio.write(f"Espaço médio ocupado: {converteByteToMegabyte(somaTudo(listaUsuarios)/len(listaUsuarios))} MB\n\n")

relatorio.close()
