"""
Construa um programa em Python utilizando o comando while para encontrar
todos os números pares entre 1 e 100.
"""

pares = []
i = 1

while i <= 100:
    if i % 2 == 0:
        pares.append(i)
    i += 1
print(f"Os números pares entre 1 e 100 são: {pares}")