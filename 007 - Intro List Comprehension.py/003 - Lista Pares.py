"""listaPares = []
for num in range(1,101):
  if num %2 == 0:
    listaPares.append(num)
print(listaPares)"""

listaPares = [num for num in range(1, 101) if num % 2 ==0]
print(listaPares)