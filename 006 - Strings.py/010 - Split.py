"""
Portanto, se aplicarmos a função split() na variável “nome”, teremos como retorno uma lista com quatro strings. Perceba que o caractere de espaço, que é utilizado como divisor, não retorna como um elemento da lista.
"""

nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
print(nomes.split('/'))
#resultado: ['João Paulo', 'Maria Paula', 'Ana Beatriz', 'José Pedro']