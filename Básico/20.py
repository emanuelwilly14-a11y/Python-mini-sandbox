# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

numero = int(input('Digite um número: '))

for i in range(1,13):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado}')