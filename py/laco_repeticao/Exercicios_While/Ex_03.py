"""
Faça um programa em linguagem Python utilizando while que recebe a
temperatura de z cliente e imprima a mensagem de se a temperatura esta
normal (menor que 37,2 C) ou está em estado febril (37,3 C a 38 C )ou com
febre (38C a 39 C) e com febre alta(acima 39 C).No final mostre a quantidade
de pessoas analisadas e a média de temperatura.
"""

tem_cliente = "s"
cliente = 0
temperaturas = 0
while tem_cliente == "s":
    temperatura = float(input(f"Digite a temperatura do cliente {cliente + 1}: "))
    if temperatura < 37.2:
        print("Temperatura está normal")
    elif temperatura > 37.2 and temperatura < 38:
        print("está em estado febril")
    elif temperatura > 38 and temperatura < 39:
        print("Está com febre")
    else:
        print("Febre Alta!!")


    cliente += 1
    temperaturas += temperatura

    tem_cliente = input("Tem mais cliente? (s / n): ")
print(f"Quantidade de pessoas examinadas: {cliente}. A média de temperatura é: {temperaturas/cliente}")
