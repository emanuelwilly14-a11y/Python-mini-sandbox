# 4 - Faça um programa em Python que utilize o tratamento de exceções para ler com segurança um número inteiro fornecido pelo usuário.

def ler_numero_inteiro():
    try:
       numero = int(input('Digite um número inteiro: ')) 
       print(f'O número digitado é, {numero}')
    except ValueError:
        print('É um número invalido por favor escreva apenas números como "8"')    

ler_numero_inteiro()