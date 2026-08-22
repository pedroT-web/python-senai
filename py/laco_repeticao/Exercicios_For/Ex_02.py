"""
Faça um programa que leia 5 números e informe o maior número.
"""
from random import randint

maior = None

for i in range(5):
    numero = int(input(f"Digite o {i}° número: "))

    if maior is None or numero > maior:
        maior = numero

print("O maior número é: ", maior)