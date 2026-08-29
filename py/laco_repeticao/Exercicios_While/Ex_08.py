# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e
# voltando a pedir as informações.

nome = input("Digite o seu nome: ")
senha = input("Digite a sua senha: ")

while senha == nome:
    print("A senha deve ser diferente do nome")
    senha = input("Digite a senha novamente: ")

print(f"Parabéns {nome}, concluiu o seu cadastrado!!")