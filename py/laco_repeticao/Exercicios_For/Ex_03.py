"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e
50.
"""
from time import sleep
from random import randint

for i in range(1, 51, 2):
    sleep(0.5)
    print(i)