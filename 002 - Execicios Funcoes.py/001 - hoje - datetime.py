"""Desafio 2 - Faça um programa que informe a data e a hora para o usuário. Para isso use a função datetime.now() do módulo datetime."""

from datetime import datetime # de datetime importado de datetime

data_hora = datetime.now() #data_hora recebe a datetime de agora
data_hora_str = data_hora.strftime("%d/%m/%Y") # strftime() -> parâmetro a formatação que queremos em nossa string de data a ser exibida
print(f"Hoje é: {data_hora_str}")