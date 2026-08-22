"""
Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números ímpares.
"""

from random import randint
numerosPares = []
numerosImpares = []
pares = 0
impar = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}° número: "))
    if numero % 2 == 0:
        pares = pares + 1
        numerosPares.append(numero)
    else:
        impar = impar + 1
        numerosImpares.append(numero)

print("Números Pares: ", pares, "Sendo eles: ", numerosPares)
print("Números Ímpares: ", impar, "Sendo eles: ", numerosImpares)