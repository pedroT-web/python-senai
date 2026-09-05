# Faça um programa, utilizando Dicionários, que:
# 1° Passo: Peça para o usuário inserir o nome de três funcionários e
# os mostre na tela.

# 2° Passo: Peça para o usuário demitir um funcionário e mostre na
# tela os funcionários restantes.

funcionarios = {}
i = 1
print("Informe o nome de 3 funcionários")
while i <= 3:
    funcionario = input(f"Digite o nome do {i}° Funcionário: ")
    funcionarios[funcionario] = f"funcionario{i}"
    i += 1

print("Demita um funcionário")
demissao = input("Digite qual funcionário deseja demitir: ")
del funcionarios[demissao]

print("Funcionários restantes")
for funcionarios_restantes in funcionarios.keys():
    print(funcionarios_restantes)