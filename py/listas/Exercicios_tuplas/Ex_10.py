# Extraindo Informações: Crie uma tupla de alunos e notas chamada alunos_notas, 
# contendo as seguintes informações: 
#     • Aluno: "Ana" Nota: 9.5 
#     • Aluno: "João" Nota: 8.7 
#     • Aluno: "Pedro" Nota: 7.9 
# Extraia os nomes dos alunos e suas respectivas notas em duas novas tuplas separadas, 
# utilizando o conceito de desempacotamento de tuplas aninhadas. 
# Mostre os valores das tuplas extraídas.
alunos_notas = (("Ana", 9.5), ("João", 8.7), ("Pedro", 7.9))
nomes = ()
notas = ()

for nome, nota in alunos_notas:
    nomes += (nome, )
    notas += (nota, )
    
print(nomes)
print(notas)
