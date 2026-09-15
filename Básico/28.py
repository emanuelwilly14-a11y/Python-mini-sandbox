# 28 - Faça um programa em Python que leia três notas obtidas por um aluno, calcule a média aritmética entre elas e exiba a situação acadêmica do estudante.

print('Digite as 3 notas do alunos')

print('Digite a primeira nota')
nota1 = float(input())

print('Digite a segunda nota')
nota2 = float(input())

print('Digite a terceira nota')
nota3 = float(input())

notaT = nota1 + nota2 + nota3
media = notaT / 3

if media >= 7.0:
    print('Estás Aprovado com', media)

elif media >= 5.0:
    print('Estas de Recuperação com', media)

else:
    print('Estas reprovado com', media)


