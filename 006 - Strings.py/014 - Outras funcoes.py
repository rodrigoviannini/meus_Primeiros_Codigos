"""Outras funções interessantes...

isdigit()
isalpha()
isalnum()
isspace()
"""


frase = "ele disse: vamos nos encontrar às 13:00"

num = []
letra = []
spaces = []
pontos = []

for char in frase:
    if char.isdigit():
        num.append(char)
    elif char.isalpha():
        letra.append(char)
    elif char.isspace():
        spaces.append(char)
    else:
        pontos.append(char)

print(num)
print(letra)
print(spaces)
print(pontos)