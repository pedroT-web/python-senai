"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""

from random import randint

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

if num1 > num2:
    i = num2
    for i in range(num2, num1):
        print(i)
else:
    i = num1
    for i in range(num1, num2):
        print(i)
