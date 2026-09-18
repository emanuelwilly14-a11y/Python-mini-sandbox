# 3 - Faça um programa em Python que utilize uma função para determinar se um número inteiro fornecido pelo usuário é um número primo

# Erraste mas tentaste 
# def verificar(numero = int(input('Insira um número: '))):
#     if numero <= 1:
#         print(f'{numero} este numemero não é valido')
#     elif numero % numero == 0 and numero % 2 == 1:
#         print(f'{numero} True')
#     else:
#         print(f'{numero} False')

#     return numero

# verificar()

#Feito pela IA
def eh_primo(numero):
    if numero <= 1:
        return False
    
    # Testa se o número é divisível por qualquer valor de 2 até (numero - 1)
    for i in range(2, numero):
        if numero % i == 0:
            return False  # Encontrou um divisor além de 1 e dele mesmo
            
    return True  # Se passou pelo laço sem divisores, é primo!

# Exemplo de uso:
num = int(input('Insira um número: '))
if eh_primo(num):
    print(f'O número {num} é PRIMO! (True)')
else:
    print(f'O número {num} NÃO é primo. (False)')