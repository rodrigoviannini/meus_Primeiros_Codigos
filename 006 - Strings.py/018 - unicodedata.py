"""Podemos usar as funções acima para padronizar a resposta de um usuário!

Utilizamos a função

unicodedata.normalize("NFD", minha_string).encode("ascii", "ignore").decode("utf-8")

Para tirar acentos da string "minha_string"

E o strip() é usado pra tirar espaços desnecessários do início e do fim de uma string
"""

import unicodedata

# mais um exemplo

minha_string = "Coração"

print()
print("string original:", minha_string)
print()
print("string padronizada:", unicodedata.normalize("NFD", minha_string).encode("ascii", "ignore").decode("utf-8").upper().strip())
print()