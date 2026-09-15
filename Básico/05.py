# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

min_salario = 1293.20

salario = float(input('Digite o seu salario atual: '))

resultado = round(salario / min_salario, 5) 

print(f'Você recebe {resultado} de salario minimo')

# ou

# min_salario = 1293.20

# salario = float(input('Digite o seu salario atual: '))

# resultado = salario / min_salario 

# print(f'Você recebe {resultado:.5f} de salario minimo')