cont = 0

while cont < 10:
    if 3 < cont <6:
        cont = cont +1 # Para o continue não gerar um looping infinito
        continue # Para o codigo no ==2 e continua
    print(cont)
    cont = cont + 1
else:
    print("Acabou!")