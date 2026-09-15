# 27 - Faça um programa em Python que receba um número inteiro do usuário e verifique se ele é par ou ímpar.

print('Digite uma número para saber se ele é par ou impar')
n1 = int(input())
def numero():
    if n1 % 2 == 0:
        print('O numero é',n1, 'par')
    else:
        print('O numero é',n1, 'impar')

numero()
