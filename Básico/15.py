# 15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.

# (Ex: 5 anos, 2 meses e 15 dias de vida)
from datetime import datetime

ano_nascimento = int(input('Digite o teu ano de nascimento: '))
ano_atual = datetime.now().year

ano = ano_atual - ano_nascimento
meses = ano * 12
dia = meses * 30

print(f'Estas vivo a {ano} anos, {meses} meses e {dia} dias ')