"""O dia e horário de matrícula dos calouros da PUC depende do curso desejado. Faça um programa que utilize duas listas, descritas abaixo:

1. Lista de Cursos: Cada elemento é uma sublista com três elementos: o primeiro é o nome do curso, o segundo é a data de matrícula e o terceiro elemento é o numero de aprovados no curso;

2. Lista de Aprovados: Cada elemneto é uma sublista com três elementos: o primeiro é o nome do aluno, o segundo é o nome do curso e o terceiro elemento é a colocação no vestibular.

O programa deve exibir, para cada aluno, seu nome, seu curso, dia e horário de matrícula e horário. Os alunos são divididos em 4 grupos de acordo com sua colocação. O primeiro grupo é compostos pelos melhores colocados (1/4 do total de vagas), o segundo grupo pelos seguintes melhores colocados (1/4 seguinte do total de vagas), e assim, sucessivamente.

Por exemplo: Um curso com 100 vagas, do 1º ao 25º colocado pertence ao grupo 1, do 26º ao 50º colocado, pertence ao grupo 2, o 51º ao 75º colocados pertencen ao grupo 3 e do 76º ao 100º colocados pertencem ao grupo 4.

Há horários possíveis: 1º -> 8 as 11h30 | 2º -> 12 as 13h30 | 3º -> 14 as 15h30 | 4º -> 16 as 17h30"""

# CRIAÇÃO DA LISTA

listaAprovados = [
    ["Luis", "Computação",  "13/10/2021", 40, 39],
    ["Brian", "Computação",  "13/10/2021", 40, 6],
    ["Larissa", "Computação",  "13/10/2021", 40, 3],
    ["Vitor", "Geografia", "12/10/2021", 20, 19],
    ["Mauricio", "Geografia", "12/10/2021", 20, 11],
    ["Guilherme", "Design",  "12/10/2021", 80, 25],
]

# WHILE
i = 0
while (i < len(listaAprovados)):
    # print(listaAprovados[i])
    print("Nome: ", listaAprovados[i][0])
    print("Curso: ", listaAprovados[i][1])
    print("Data: ", listaAprovados[i][2])
    
    limiteUm = listaAprovados[i][3] // 4
    limiteDois = listaAprovados[i][3] // 4 * 2
    limiteTres = listaAprovados[i][3] // 4 * 3
    limiteQuatro = listaAprovados[i][3] // 4 * 4
    colocacao = listaAprovados[i][4]
    
    
    # IF

    if colocacao <= limiteUm:
        print("Primeiro horário de 8 as 11h30min\n")
    elif colocacao <= limiteDois:
        print("Segundoo horário de 12 as 13h30min\n")
    elif colocacao <= limiteDois:
        print("Terceiro horário de 14 as 15h30min\n")
    else:
        print("Quarto horário de 16 as 17h30min\n")


    i += 1