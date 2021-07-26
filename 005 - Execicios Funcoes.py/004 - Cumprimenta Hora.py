def cumprimentaHora(nome, hora):

    if hora < 12:
        return "Bom dia, " + nome
    elif hora < 19:
        return "Boa tarde, " + nome
    else:
        return "Boa noite, " + nome
    

texto = cumprimentaHora(input("Digite seu nome: ").title(), int(input("Digite a hora com 1 ou 2 casas: ")))
print(texto)