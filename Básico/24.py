# 24 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

# Fórmula: distância = tempo x velocidade.
# litros usados = distância / 12.
tempo = int(input('Digite quantas horas foram de viagem: '))
velocida = int(input('Digite a velocidade usada: '))

d_percorrida = velocida * tempo

litros_usados = d_percorrida / 12


print(f'A velocidade media é de {velocida}, tempo gasto de {tempo}, distancia percorrida de {d_percorrida} e a quantidade de litros usados é de {litros_usados}')