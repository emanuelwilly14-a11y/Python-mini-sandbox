# 5 - Faça um programa em Python que utilize um dicionário estruturado com listas paralelas para gerenciar e exibir etiquetas formatadas de produtos de um inventário.


# produto = {
#     "nome: " : ["Computador", "Lampada", "Teclado Metalico"], 
#     "Preço: " : ["22.000.00", "150.00", "25.000.00"],
#     "Estoque: " : [20, 120, 15]
# }
# # print("\n".join(produto["nome"]))
# def em_estoque():
#     print("==Etiqueta dos produtos==")

#     for chave, valor in produto.items():
#         print(f'\n{chave}', f'\n{valor})' ) 
#     return produto

# em_estoque()


produto = {
    "nome": ["Computador", "Lampada", "Teclado Metalico"], 
    "Preço": ["22.000,00", "150,00", "25.000,00"],
    "Estoque": [20, 120, 15]
}

def exibir_etiquetas(dados):
    print("=== ETIQUETAS DOS PRODUTOS ===")
    
    # Descobrimos quantos produtos existem na lista
    total_produtos = len(dados["nome"])
    
    for i in range(total_produtos):
        print(f"\n--- Produto {i+1} ---")
        print(f"Nome: {dados['nome'][i]}")
        print(f"Preço: R$ {dados['Preço'][i]}")
        print(f"Estoque: {dados['Estoque'][i]} unidades")

exibir_etiquetas(produto)