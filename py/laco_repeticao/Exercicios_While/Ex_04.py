"""
Ler do teclado a idade e o sexo de N pessoas, calcule e imprima:
•idade média das mulheres
•idade média dos homens
•idade média do grupo
"""

n_pessoas = 0
n_homens = 0
n_mulheres = 0
proximo = "s"
totalIdadeMasc = 0
totalIdadeFem = 0
totalIdades = 0
while proximo == "s":
    sexo = input("Digite seu sexo(Masc - Homen / Fem - Mulher)")
    idade = int(input("Digite sua idade: "))

    totalIdades += idade

    if sexo == "Masc":
        totalIdadeMasc += idade
        n_homens += 1
    elif sexo == "Fem":
        totalIdadeFem += idade
        n_mulheres += 1
    else:
        print("Gênero Incorreto!!!")

    proximo = input("Tem Próximo?(s / n) ")
n_pessoas = n_homens + n_mulheres

print(f"A idade média entre os homens é: {totalIdadeMasc / n_homens}")
print(f"A idade média entre as mulheres é: {totalIdadeFem / n_mulheres}")
print(f"A idade média entre os homens e as mulheres é: {totalIdades / n_pessoas}")
        