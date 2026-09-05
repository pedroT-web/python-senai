# Faça um programa, utilizando Dicionários, que peça para o
# usuário inserir o nome de três produtos de mercado e seus
# respectivos preços e os mostre na tela.

i = 0
produtos = {}
while i < 3:
    nome_produto = input(f"Digite o nome do {i + 1}° produt: ")
    valor_produto = float(input(f"Digite o valor do(a) {nome_produto}: "))
    produtos[nome_produto] = valor_produto
    i += 1
print(produtos)
     