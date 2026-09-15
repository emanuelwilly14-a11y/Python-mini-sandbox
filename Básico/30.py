# 30 - Faça um programa em Python que receba cinco números do usuário, armazene-os em uma lista e utilize estruturas de repetição para realizar comparações entre eles.

print('Insira 5 numeros')

lista = [float(input()), float(input()), float(input()), float(input()), float(input())]

for i in range(5):
    for e in range(5):
        if lista[i] > lista[e]:
            print('O maior numero é', lista[i])
            break
        
        if lista[i] < lista[e]:
            print('O menor mumero é', lista[i])
            break

