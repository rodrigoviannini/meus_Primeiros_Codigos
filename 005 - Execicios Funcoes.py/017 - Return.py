def somar(a=0,b=0,c=0):
  s = a+b+c
  return s

r1 = somar(3,2,5)
r2 = somar(8,4) # a=b=c=0 parametro opcional
r3 = somar(4)

print(f'As somas valem: {r1}, {r2}, {r3}')