# Remover Duplicatas de uma Lista:
# Escreva um programa que remova as duplicatas de uma lista, preservando a ordem
# original dos elementos.

lista_duplicada = [2, 5, 2, 3, 4, 6]
lista_correta = []

for item in lista_duplicada:
    if item not in lista_correta:
        lista_correta.append(item)
print(f"Lista com repetições: {lista_duplicada}")
print(f"Lista sem repetições: {lista_correta}")