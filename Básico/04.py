# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

import time
while True:
    try:
        numero = int(input('Digite um nuemro: '))

        sucessor_numero = numero + 1
        antecessor_numero = numero - 1

        print(f'O seu numero é {numero}, o seu sucessor é {sucessor_numero} e o seu antecessor é {antecessor_numero}')
        break 

    except ValueError:
        print('Digite apenas números inteiros')
        time.sleep(1)
