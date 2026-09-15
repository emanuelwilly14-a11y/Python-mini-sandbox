# 14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

A = input('Digite um valor qualquer para A: ')
B = input('Digite outro valor qualquer para B: ')

A,B = B,A

print(f'O valor de A é {A} e o valor de B é {B}')