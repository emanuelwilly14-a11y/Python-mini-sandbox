#Erraste mas tentaste fica com ele para sentores vergonha o certo fi feito com IA
# print('Digite 6 números')

# for i in range(1, 7):

#     r = int(input())

#     p = r % 2 == 0
#     o = r % 2 != 0
#     soma = p

# print('Estes numeros são pares, ', p)
# print('Estes é a soma dos numeros pares, ',soma)
# print('Estes numeros são impares, ',o)
   
# Inicializamos os contadores e a soma antes do laço
qtd_pares = 0
qtd_impares = 0
soma_pares = 0

print('Digite 6 números:')

for i in range(6):
    numero = int(input())
    
    if numero % 2 == 0:
        qtd_pares += 1          # Incrementa a contagem de pares
        soma_pares += numero    # Acumula o valor na soma dos pares
    else:
        qtd_impares += 1        # Incrementa a contagem de ímpares

# Exibimos os resultados FORA do laço
print('Quantidade de pares:', qtd_pares)
print('Quantidade de ímpares:', qtd_impares)
print('Soma de todos os números pares:', soma_pares)
