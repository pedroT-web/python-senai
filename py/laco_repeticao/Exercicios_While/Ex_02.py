"""
Faça um programa em Python (utilize a estrutura while) que leia 10
valores inteiros e:
• Encontre e mostre o maior valor
• Encontre e mostre o menor valor
• Calcule e mostre a média dos números lidos
"""

i = 1
maior = None
while i <= 10:
    numero = int(input("Digite um número: "))
    if maior is None or numero > maior:
        maior = numero
    i += 1
print(f"O maior número digitado é: {maior}")