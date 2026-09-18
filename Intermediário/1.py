# 1 - Faça um programa em Python que funcione como uma calculadora de frações utilizando a biblioteca padrão para garantir exatidão matemática.

from fractions import Fraction #Permite transformar os números em frações

n = Fraction(int(input('Digite o númerador: ')), int(input('Digite o Denominador: ')))

i = input('Digite o tipo de operação:')

n2 = Fraction(int(input('Digite o númerador: ')), int(input('Digite o Denominador: ')))
match i:
    case "*":
        r = n*n2
        print(f'O resultado da multplicação de {n} e {n2} é {r}')
    case "+":
        r = n+n2
        print(f'O resultado da soma de {n} e {n2} é {r}')
    case "-":
        r = n - n2
        print(f'O resultado da multplicação de {n} e {n2} é {r}')
    case "/":
        r = n/n2
        print(f'O resultado da divisão de {n} e {n2} é {r}')
    case _:
        print('Só é valido *,/,+ e -')