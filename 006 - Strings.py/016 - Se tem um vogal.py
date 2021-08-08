def possuiVogais(string):
    for letra in string:
        if letra.lower() in 'aeiou':
            return True
    return False

print(possuiVogais("pss vgs"))