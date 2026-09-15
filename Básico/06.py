# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

numero = float(input('Digite um número: '))

resultado = numero * 0.05
valor_final = resultado + numero

print(f'O número {numero} tem um ajuste de 5% com o resultado {resultado:.5} e tem como valor final {valor_final}')