# 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é equilátero, isósceles ou escaleno.

lado1 = int(input('Digite um dos lados do triangulo: '))
lado2 = int(input('Digite o segundo lado do triangulo: '))
lado3 = int(input('Digite o terceiro lado do traingulo: '))

if lado1 == lado2 == lado3:
    print('Este é um triangulo Equilátero')
elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 !=lado1:
    print('Este é um traingulo Isósceles')
elif lado1 != lado2 != lado3:
    print('É um triagulo Escaleno')
