def somaTudo(lista):
    soma = 0
    for colaborador in lista:
        soma += int(colaborador[1])
    return soma

def converteByteToMegabyte(nrBytes):
    return int(nrBytes)/(2**20)

def calculaPorcentagem(lista, tamanho):
    return int(tamanho)/somaTudo(lista)*100

usuarios = open("usuarios.txt", "r", encoding="utf-8")

listaUsuarios = []
for usuario in usuarios:
    listaUsuarios.append(usuario.split())

usuarios.close()

relatorio = open("relatorioFormatado.txt", "w", encoding="utf-8")
relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
relatorio.write("------------------------------------------------------------------------\n")
relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

# listaUsuarios = sorted(listaUsuarios, key=lambda x : int(x[1]))
listaUsuarios = sorted(listaUsuarios, key=lambda x : x[0])

for idx, colaborador in enumerate(listaUsuarios):
    texto = "{:<5d}{:<15}{:>13.2f} MB{:>12.2f}%\n".\
        format(idx+1, colaborador[0].capitalize(), converteByteToMegabyte(colaborador[1]), calculaPorcentagem(listaUsuarios, colaborador[1]))

    relatorio.write(texto)

relatorio.write("\nEspaço total ocupado: {:.2f} MB\n".format(converteByteToMegabyte(somaTudo(listaUsuarios))))
relatorio.write("Espaço médio ocupado: {:.2f} MB".format(converteByteToMegabyte(somaTudo(listaUsuarios)/len(listaUsuarios))))

relatorio.close()

