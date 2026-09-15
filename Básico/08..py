# Desafio 8: Soma de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i
print("A soma de 1 a 100 é:", soma)  # Resultado: 5050

# Desafio 10: Maior e Menor valor
lista = []
print("Insira 5 números:")
for i in range(5):
    lista.append(float(input()))

# Usando as funções nativas min() e max():
print("O maior número é:", max(lista))
print("O menor número é:", min(lista))