# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo com a tabela abaixo:

# Fórmula do IMC = peso / (altura) ²

# Tabela Condições IMC

  

#  Abaixo de 18,5   | Abaixo do peso          

#  Entre 18,6 e 24,9 | Peso ideal (parabéns)  

#  Entre 25,0 e 29,9 | Levemente acima do peso

#  Entre 30,0 e 34,9 | Obesidade grau I 

#  Entre 35,0 e 39,9 | Obesidade grau II (severa)

#  Maior ou igual a 40 | Obesidade grau III (mórbida)



print('Digite as informações pedidas para o calculo do seu IMC\n')

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura ** 2)

print(f'O seu IMC é de {imc:.1f}')

if imc <= 18.5:
    print('Estás abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print('Estas no peso ideal')
elif 25.0 <= imc <= 29.9:
    print('Sobrepeso, estás acima do peso')
elif 30.0 <= imc <= 34.9:
    print('obesidade grau 1.')
elif 35.0 < imc < 39.9:
    print('obesidade grau 2.')
elif imc > 40.0:
    print('obesidade grau 3 (obesidade grave)')