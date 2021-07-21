# FATORIAL - WHILE

num = int(input("Fatorial de: ") )

result = 1
cont = 1

while cont <= num:
    result *= cont
    cont += 1

print(result)