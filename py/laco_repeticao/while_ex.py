"""
Faça um programa que exiba os números de 50 a 1000.
"""

# i = 50

# while i <= 1000:
#     print(i)
#     i += 1


"""
Escreva um progama que peça ao usuário um número e realize uma contagem regressiva de 10 em 1 até o número digitado, finalizando com a mensagem "Cheguei!!!"
"""

# limite = int(input("Digite um número menor que 10: "))
# contador = 10

# while contador >= limite:
#     print(contador)
#     contador -= 1 # Contagem regressiva

# print("Cheguei!!!")


"""
Escreva um programa que peça ao usuário um número inteiro positivo N e calcule a soma dos N primeiros números naturais (1 + 2 + 3 + ... N)
"""

n = int(input("Digite um número inteiro positivo: "))
soma = 0 
i = 1

while i <= n:
    soma += i # Adicionar o valor atual de i na variável
    i += 1 
print(f"A soma dos primeiros {n} números é: {soma}")