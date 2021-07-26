# Uma frase e uma letra
# Contar aquela letra na frase especificada

def contaLetra(frase, letra):
    fraseMinusculo = frase.lower()
    letraMinusculo = letra.lower()

    contagemLetra = 0
    for l in fraseMinusculo:
        if l == letraMinusculo:
            contagemLetra += 1

    return contagemLetra

frase = "Bom dia , cOmo vaI vOce?"
letra = "o"
print(f'\n\n || A qtde de letras "{letra}" na frase: "{frase}" são  de: {contaLetra(frase, letra)}', 'letras ||\n\n')