"""TRATAMENTO DE ERROS | TRY and EXCEPT"""

try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  r = a / b

except (ValueError, TypeError):
  print('Tivemos um problema com o tipo de dados que você digitou!')

except ZeroDivisionError:
  print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
  print('O usuário preferiu não informar os dados!')

except exception as erro:
  print(f'O erro encontrado foi {erro.__cause__}')

else: 
  print(f'O resultado é {r:.2f}')

finally:
  print('Volte sempre! Muito obrigado!')