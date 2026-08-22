# Importar a função 'randint' da biblioteca 'random' para gerar números alearórios
from random import randint

# Importar a função 'sleep' do modulo 'time' para pausar a execução do programa por alguns segundos.
from time import sleep

# Criar uma tupla com opções do jogo (0: PEDRA, 1: PAPEL, 2: TESOURA)
itens = ('Pedra', 'Papel', 'Tesoura')

# Sorteia um número inteiro aleatório entre 0 e 2, representando a jogada do computador
computador = randint(0,2)

print('''Suas opções: 
[0] - Pedra
[1] - Papel
[2] - Tesoura
''')
jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("=" * 12)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print("=" * 12)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
else:
    print("JOGADA INVÁLIDA PARA AMBOS")