"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

from random import randint

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
soma = 0
cont = 0

if num1 > num2:
    i = num2
    for i in range(num2, num1):
        print(i)
        cont =+ i
        soma = soma + i
else:
    i = num1 + 1
    for i in range(num1, num2):
        print(i)
        cont =+ i
        soma = soma + i

print(f"A soma dos {cont} números que estão entre {num1, num2} é: {soma}")
