def title(string):
    stringNova = string[0].upper() # Já começo a primeira string em maiusculo
    for i in range(1, len(string)): # Começo no index 1, varrendo do primeiro index para frente
        if string[i-1] == ' ': # Posição anterior sendo um espaço
            stringNova += string[i].upper() # concatenando e atribuindo
        else:
            stringNova += string[i].lower() # Se nao tiver espaço mantem minusculo
    return stringNova

print(title("essa turma é bRAba!"))