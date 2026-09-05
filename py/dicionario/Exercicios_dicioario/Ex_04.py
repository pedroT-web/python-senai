# Faça um programa, utilizando Dicionários, que:
# 1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa
# Misteriosa”.

# 2° Passo: Peça para o usuário inserir um número.

# 3° Passo: Mostre na tela o que foi inserido na posição do número
# inserido pelo usuário.

caixa_misteriosa = {}
i = 1
while i <= 4:
    objeto = input("Insira alguma coisa na caixa misteriosa: ")
    caixa_misteriosa[i] = objeto

    i += 1
numero_escolhido = int(input("Digite um número de 1 a 4: "))

print(f"O item na posição {numero_escolhido} é {caixa_misteriosa[numero_escolhido]}")