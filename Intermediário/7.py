#  7 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

#  Tabela de Código de Condições de Pagamento

#  1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

#  2 - À Vista no cartão de crédito, recebe 10% de desconto

#  3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

#  4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
import time

while True:
    preço = 150000
    print('\nO PC está custando 150.000.00 qual será a forma de pagamento?\n')
    time.sleep(1)

    print('1. À Vista em Dinheiro ou Pix\n2. À Vista no cartão de crédito\n3. Parcelado no cartão em duas vezes\n4. Parcelado no cartão em três vezes ou mais\n')

    escolha = int(input('Digite o número da escolha do tipo de pagamento: '))

    match escolha:
        case 1:
            desconto = preço * 0.15
            preço_final = preço - desconto
            print(f'Recebeste 15% de desconto então o preço final a pagar é de {preço_final} ')

        case 2:
            desconto = preço * 0.10
            preço_final = preço - desconto
            print(f'Tens 10% de desconto então o preço a se pagar é de {preço_final}')

        case 3:
            print(f'O preço a se pagar é de {preço}')
            
        case 4:
            t = int(input('Digite as vezes que vais querer parcelar no cartão: '))
            if t >=3:
                j = preço * 0.10
                preço_com_juros = preço + j
                valor_parcela = preço_com_juros / t
                print(f'O preço a se pagar é de {valor_parcela:.0f} durante {t} meses, os juros são de {j:.0f}')
            else:
                print(f'Por favor escolhe a opção 2')
        case _:
            print('\n\033[31mEstá opção não está disponivel\033[0m')
    time.sleep(2)
    break