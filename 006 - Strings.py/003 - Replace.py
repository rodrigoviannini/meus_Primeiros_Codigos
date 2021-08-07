def replace(string, ant, novo):
    novaString = ''
    for letra in string:
        if letra == ant:
            novaString += novo # Vou concaternar o que eu quero substituir
        else:
            novaString += letra # Vou concaternar com a própria letra
    return novaString

# replace(string, ant, novo)
print(replace("ABBBBCDDBBE", "B", "N"))