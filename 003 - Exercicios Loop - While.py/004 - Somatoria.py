"""Somatoria de: 1/1 + 1/2 + 1/3 ... 1/1000"""

somatoria = 0
contador = 1

while contador <= 1000:
    somatoria += 1/contador
    contador += 1

print("Somatoria", round(somatoria, 3))