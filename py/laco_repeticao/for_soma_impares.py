"""
Faça um programa que calcule a soma entre os números ímpares que são múltiplos de 3
e que se encontram no intervalo de 1 a 500 
"""

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0: # Números ímpares divisivel por 3
        cont = cont + 1 
        soma =+ i
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))