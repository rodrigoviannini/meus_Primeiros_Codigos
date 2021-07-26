"""
Break point - ponto vermelho onde quero parar o debug/ depurar

Comandos principais : 
=> Continuar: Continue!
=> Step Over: Pula uma linha, se tiver uma função, ele pula função toda até a primeira linha subsequênte!
=> Stop/ Intervir: Entra dentro da função! 
=> Step Out: [Call Stack]
=> Restart: Reinicia o código do zero
=> Stop: Finaliza o Debug

BREAKPOINT -> soma
    F10 -> Crio a variável soma = 0 
    VARIABLES | LISTA | SOMA: 0 [tela à esquerda] -> altera SOMA e NUM
    SEQUÊNCIAS-> Aperta F!0 e analisa o código passo-a-passo!

"""


lista = [1, 4, 5, 2, 9, 4, -10, 8]

soma = 0
for num in lista:
    soma += num

print(soma)
