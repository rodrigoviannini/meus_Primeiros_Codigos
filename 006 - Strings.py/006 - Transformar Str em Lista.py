# Transformar uma string em uma lista
login = "s.o.u.e.u.r.o.d.r.i.g.o"
print(list(login))

# Tirar os pontos
login = "s.o.u.e.u.r.o.d.r.i.g.o"
novoLogin = login.split(".")
print(novoLogin)

# Transformar em string

login = login.replace(".", ' ')
print(login)