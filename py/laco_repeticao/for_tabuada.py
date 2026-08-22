""" Mostrar a tabuada de um número que o usuário escolher, só que utilizando o laço for """

num = int(input("Digite um número para ver sua tabela: "))
for i in range(1, 11):
    print("{} X {} = {}".format(num, i, num*i))