'Faça um script que faça o login de uma pessoa no servidor ABC. Um usuário é "admin" e a senha é "admin123".'

# LOGIN
usuarioCorreto = "admin" 
usuario = str(input("Digite seu login: "))

contadorLogin = 0


while usuario != "admin":
    contadorLogin += 1
    print("Você digitou um login inválido, tente novamente! [Verifique se a tecla CAPSLOOK esteja acionada!]")
    usuario = str(input("Digite seu login: ")) # Faz com que o looping não seja infinifto e o programe, pergunte novamente até que o login seja o correto.
    # Enquanto não colocar o LOGIN correto, não irá acessar o campo SENHA!
    
# SENHA    
senhaCorreta = "admin123"
senha = str(input("Digite sua senha: "))

contadorSenha = 0
    
while senha != "admin123":
    contadorSenha += 1
    print("Você digitou uma senha inválida, tente novamente! [Verifique se a tecla CAPSLOOK esteja acionada!]")
    senha = str(input("Digite sua senha: "))
    # Enquanto não colocar a SENHA correta, não irá liberar o acesso!
    
else:
    print("Acesso liberado!")
    # O acesso estará LIBERADO após atendida tanto a condição de LOGIN quanto a SENHA, respectivamente!