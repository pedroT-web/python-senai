# Escreva um programa em Python para encontrar o fatorial de qualquer número.
numero = int(input("Digite um número inteiro: "))

i = 1
while numero != i:
    calculo = numero * i
    print(f"{numero} X {i} = {calculo}")
    if numero > i:
        i += 1
    elif numero < i:
        i -= i
    else:
        print("Acabou")
