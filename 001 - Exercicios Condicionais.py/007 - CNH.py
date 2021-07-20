"Faça um script que informe se uma pessoa está pronta para dirigir um carro."
"Uma pessoa só pode dirigir se for maior de idade e se tiver carteira de motorista." 
"Dica: carteira pode ser variável lógica."

# IDADE
idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Você tem a idade mínima para dirigir")

    
# HABILITAÇÃO    
    cnh = str(input("Você possui CNH-B, digite S [SIM] ou N [NÃO]: ")).upper()

    if cnh == "S":
        print("Você é habilitado!")
    else:
        print("Você não está apto à dirigir, espere atingir os requesitos mínimos")
        
else:
    print("Você não tem idade para dirigir") 