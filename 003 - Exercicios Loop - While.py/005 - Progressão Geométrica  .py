"""Progressão Geométrica de: 1/1 + 1/2 + 1/3 ... 1/1000"""
# Sempre será igual a 2

somatoria = 0
contador = 1
fator = 1

while contador <= 1000:
    somatoria += 1/fator
    fator *= 2
    contador += 1

print("Somatoria", round(somatoria, 3))