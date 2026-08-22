import random
numero_secreto = random.randint(1, 100)
tentativas = 0
limite_tentativas = 34
acertou = False

print(f"--------- Jogo da Adivinhação (Máximo {limite_tentativas} de tentativas) ---------")

while tentativas < limite_tentativas:
    palpite = int(input(f"{tentativas + 1} Tentativa de {limite_tentativas} tentativas. Seu palpite: "))
    tentativas += 1 # Aumenta o contador a cada rodada

    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print(f"Acertou em {tentativas} tentativas, parabéns!!!")
        acertou = True
        break # Sai do loop imediatamente se acertar
# Condição final caso as tentativas acabem e ele não tenha acertado
if not acertou:
    print(f"\n Suas tentativas acabaram! O número era {numero_secreto}. Game Over!!!")
        