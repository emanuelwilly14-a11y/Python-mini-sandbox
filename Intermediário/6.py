#  6 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

import time
while True:
    try:
        qnt_alunos = int(input('Digite quantos alunos vais calcular a média: '))

        for i in range(qnt_alunos):

            aluno_nome = input('Digite o nome do aluno: \n')
            nota1 = float(input(f'Digite a primeira nota do {aluno_nome}: '))
            nota2 = float(input(f'Digite a segunda nota do {aluno_nome}: '))
            nota3 = float(input(f'Digite a terceira nota do {aluno_nome}: '))
            nota4 = float(input(f'Digite a quarta nota do {aluno_nome}: '))

            media = (nota1 + nota2 + nota3 + nota4)/4

            Aluno = {
                "nome" : aluno_nome,
                "aluno_media" : media
            }
            if media >=7:
                print(f'{Aluno["nome"]}, foste aprovado com a media de  {Aluno["aluno_media"]} \n')
            else:
                print(f'{Aluno["nome"]} foste reprovado com a media de {Aluno["aluno_media"]}\n')
                break

    except ValueError:
        print('Por Favor ponha as nota e a quantidade de alunos em números inteiros ou naturais')
        time.sleep(2)