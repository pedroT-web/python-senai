# Jogo da adivinhação:
# Crie uma função que gere um número aleatório entre 1 e 100 e desafie o usuário a adivinhá-lo. 
# A função deve fornecer dicas como "maior", "menor" ou "acertou" até que o usuário acerte o número.
import random 
numero_aleatorio = random.randint(1, 100)
def adivinha(num):
    chute = 0
    
    while chute != num:
        chute = int(input("De um palpite: "))
        
        if chute > num:
            print("Menor!!")
        elif chute < num:
            print("Maior!!")
        else:
            print("Parabéns, numero correto!!")
            print(f"O número era: {num}")

adivinha(numero_aleatorio)
            