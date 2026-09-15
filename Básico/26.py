# 26 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

A = float(input('Digite um número para ser o valor A: '))
B = float(input('Digite um número para ser o valor B: '))
C = float(input('Digite um número para ser o valor C: '))

def soma():
    R = A + B
    if R < C:
        print(f'O resultado da soma é {R} e ele é menor que é o valor de C= {C}')
    elif R == C:
         print(f'O resultado da soma é {R} e o resultado {R} é igual que ao valor de C= {C} ')
    else:
        print(f'O resultado da soma é {R} e {R} é maior que o valor de C= {C} ')
        return R
soma()