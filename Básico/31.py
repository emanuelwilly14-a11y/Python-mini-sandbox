# 31 - Faça um programa em Python que receba um número do usuário e exiba na tela a sua respectiva tabuada de multiplicação de 1 até 12.

print('Insira um número para mostrar a tabuada dele')
n = float(input())
for i in range(1, 13):
    r = i * n 
    print('A tua tabela é,', n, 'x', i,'=',r)   
    