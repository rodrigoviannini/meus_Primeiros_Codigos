"""
Break point - ponto vermelho onde quero parar o debug/ depurar

Comandos principais : 
=> Continuar: Continue!
=> Step Over: Pula uma linha, se tiver uma função, ele pula função toda até a primeira linha subsequênte!
=> Stop/ Intervir: Entra dentro da função! 
=> Step Out: [Call Stack]
=> Restart: Reinicia o código do zero
=> Stop: Finaliza o Debug

BREAKPOINT -> print(fibonacci(n))
    OBS: Não posso usar o STEP OVER

    F10 -> Crio a variável soma = 0 
    VARIABLES | LISTA | SOMA: 0 [tela à esquerda] -> altera SOMA e NUM
    SEQUÊNCIAS-> Aperta F!0 e analisa o código passo-a-passo!

WATCH -> Adiciono as informações que quero visualizar dentro do FOR
    n == 1
    fib[i-1]
    fib[i-2]
    fib[i-1] + fib[i-2]

"""
# f(x) = f(x-1) + f(x-2)

# FUNÇÃO -> Vou receber um (n) |Espero que minha função retorne uma lista com (n) elementos da sequência de Fibonacci!

def fibonacci(n): 
    fib = [0,1] # Os dois primeiros argumentos da minha função são constantes!
    
    # Qual a menor opção de (n) que pode me devolver? [menor n == 1]
    if n == 1: 
        return fib[:1] # SLICE -> Até o 1o elemento! (Primeiro elemento - 0) == 1
    
    # Se for > 1, caso contrário, para cada elemento da lista, além dos dois primeiros, faço um FOR
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

n = int(input("Digite a quantidade de elementos que deseja: "))
print(fibonacci(n)) # Imprimo aquilo que sair da função!