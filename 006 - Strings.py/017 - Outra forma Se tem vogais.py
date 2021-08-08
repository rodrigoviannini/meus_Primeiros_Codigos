def possuiVogaisInLine1(string):
    return len([letra.lower() for letra in string if letra.lower() in 'aeiou']) > 0 # Garante um BOOLEAN

def possuiVogaisInLine2(string):
    return True if True in [letra.lower() in 'aeiou' for letra in string] else False

print(possuiVogaisInLine1("pssa vgs"))
print(possuiVogaisInLine2("nepd mspas"))