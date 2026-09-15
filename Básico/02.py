# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

numero = int(input('Digite um número: '))

if numero %2 == 0:
    if numero >= 0:
        print(f'O numero {numero} é par e positivo')
    else:
        print(f'O numero {numero} é par e negativo')

if numero %2 != 0:

    if numero >= 0:
        print(f'O numero {numero} é impar e positivo')
    else:
        print(f'O numero {numero} é impar e negativo')