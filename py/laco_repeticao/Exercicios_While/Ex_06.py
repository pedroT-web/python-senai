# Escreva um programa em Python que receba uma string do usuário e mostre
# de trás para frente.

texto = input("Digite algum texto: ")
texto_invertido = texto[::-1]
print("Seu texto invertido: ", texto_invertido)

# ou

texto_invertido_join = "".join(reversed(texto))