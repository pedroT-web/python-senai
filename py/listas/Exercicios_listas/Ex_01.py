# Calcular a Média de uma Lista:
# Crie um programa que receba uma lista de números e retorne a média dos valores
# presentes na lista.

lista_numeros = list(range(10))
qtdNumeros = len(lista_numeros)
soma = sum(lista_numeros)

media = soma / qtdNumeros

print(f"A média entre os valores nessa lista é: {media}")