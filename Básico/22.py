# 22 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

a = int(input('Digite um número: '))
b = int(input('Digite o segundo número: '))

quociente = a / b
resto = a % b

print(f'A divisão entre {a} e {b} tem como quociente {quociente} e resto {resto}')