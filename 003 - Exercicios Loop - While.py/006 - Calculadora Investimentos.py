"""Faça uma calculadora de investimentos que define se um fundo gera lucro real (rendimento acima da inflação) ao final de 12 meses, considerando o rendimento mensal projetado, a taxa de administração do fundo, a inflação no ano, come-cotas (vamos considerar 15%) e o capital invesido. Caso positivo informe quanto foi esse lucro."""

capitalInicial = float(input("Capital Inicial: "))
rendimentoMensal = float(input("Rendimento Mensal: "))
taxaAdm = float(input("Taxa de Administração: "))
inflacao = float(input("Inflação: "))

capitalAtual = capitalInicial

meta = capitalInicial * (1 + inflacao)

contador = 0

while contador < 6:
    capitalAtual *= (1 + rendimentoMensal)
    contador += 1

capitalAtual *= (1 - taxaAdm)
capitalAtual -= (capitalAtual - capitalInicial) * 0.15

contador = 0

while contador < 6:
    capitalAtual *= (1 + rendimentoMensal)
    contador += 1

capitalAtual *= (1 - taxaAdm)
capitalAtual -= (capitalAtual - capitalInicial) * 0.15

if capitalAtual > meta:
    print("A meta foi batida com lucro de: R$ ", capitalAtual - meta)
else:
    print("A meta não foi batida com diferença de: R$ ", capitalAtual - meta)