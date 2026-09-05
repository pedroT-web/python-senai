# Faça um programa, utilizando Dicionários, que peça para o
# usuário inserir quatro notas e mostre na tela as notas e a média entre
# elas.

i = 0
notas = {}
totalNotas = 0 
while i < 4:
    nome = input(f"Digite o nome do {i}° aluno: ")
    nota = float(input(f"Digite a nota do(a) {nome}: "))
    notas[nome] = nota
    
    i += 1

for valores_notas in notas.values():
    totalNotas += valores_notas


for aluno in notas.keys():
    print(f"Nota do(a) {aluno} é: {notas[aluno]}") 
    
media = totalNotas / 4
print("A média entre as notas é: ", media)