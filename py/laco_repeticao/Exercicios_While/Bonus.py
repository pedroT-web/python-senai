# Faça um programa que solicite ao usuário um número que ele queira treinar a
# tabuada. Você irá solicitar ao mesmo a resposta do cálculo do número informado
# multiplicado por 1, 2 até 10.
# A cada resposta você deverá validar e imprimir :”CORRETO” ou “QUE PENA,
# VOCÊ ERROU, O VALOR CORRETO É X “, no lugar
# de ”X“ coloque o valor correto Ao final imprima “Total de
# acertos: y” e “Total de erros z”, onde “y“ deverá ser o total de acertos e “z“ o total
# de erros. Ao final da sequência deve-se perguntar se deseja começar de novo.
acertos = 0
erros = 0
treino = "s"

while treino == "s":
    i = 1
    numero = int(input("Digite um número que você queira treinar a tabuada: "))
    while i <= 10:
        pergunta = int(input(f"{numero} X {i} = "))
        calculo = numero * i
        if pergunta == calculo:
            print("CORRETO")
            acertos += 1
        elif pergunta != calculo:
            print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É: {calculo}")
            erros += 1
        else:
            print("Calculo inexistente")

        i += 1

    print(f"O total de acertos é: {acertos}")
    print(f"O total de erros é: {erros}")

    treino = input("Deseja recomeçar? (s / n)")



