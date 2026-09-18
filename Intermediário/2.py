# 2 - Faça um programa em Python que utilize uma função com parâmetro padrão para inverter a ordem dos caracteres de um texto fornecido pelo usuário.

def inverter_texto(text = input('Escreva um texto para ser ivertido:')):
    texto_invertido = text[::-1]
    return texto_invertido
print(f'O seu texto invertido é: {inverter_texto()}')
