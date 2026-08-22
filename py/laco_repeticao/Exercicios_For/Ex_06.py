"""
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência
da linguagem.
"""
from random import randint
numero = []

for i in range(1, 3):
    numero.append(int(input(f"Digite o {i}° número: ")))


calculo = numero[0] ** numero[1]

print(f"{numero[0]} elevado a {numero[1]} é igual a: {calculo}")