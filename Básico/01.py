# 1. Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu
# perímetro.
from math import sqrt

print('Triangulo Retângulo\n')
base = int(input('Digite a base: '))
altura = int(input('Digite a altura: '))

area = (base * altura) / 2

e = sqrt(base**2 + altura**2) #Formula de Hipotenusa

perimetro = base + altura + e

print(f'O valor da area é de {area}, Hipotenusa = {e:.2f} e perimetro = {perimetro:.2f}')