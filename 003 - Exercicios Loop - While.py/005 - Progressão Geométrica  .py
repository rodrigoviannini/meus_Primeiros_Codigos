"""Progressão Geométrica de: 1/1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 ... 2"""
# Sempre será igual a 2

somatoria = 0
contador = 1
fator = 1

while contador < 1000:
    somatoria += 1/fator
    fator *= 2
    contador += 1

print("PG", round(somatoria, 3))