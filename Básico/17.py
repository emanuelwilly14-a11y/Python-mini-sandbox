# 17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

# Fórmula: C = (5 * ( F-32) / 9)

t_fah = float(input('Digite a temperatura em Fahrenheit: '))

C = (5 * (t_fah-32) / 9)

print(f'A temperatura em Fahrenheit é de {t_fah}°F e a temperatura em Celsius é de {C:.2f}°C')