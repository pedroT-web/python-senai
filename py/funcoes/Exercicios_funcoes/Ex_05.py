# Calculadora de IMC:
# Crie uma função que receba a altura e o peso de uma pessoa como parâmetros e retorne o 
# seu IMC (Índice de Massa Corporal).
def imc(peso, altura):
    calculo = peso / (altura**2) 
    print(f"Seu IMC atual é: {calculo}")
    
imc(80, 1.80)