#  13 - Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print(f'Parabéns {nome} és maior de idade')
else:
    print(f'{nome} não és menor de idade')