# Aninhadas: Crie uma tupla aninhada chamada agenda contendo as seguintes informações: 
# • Nome: "João" 
#     Telefone: 99999-1234 
# • Nome: "Maria" 
#     Telefone: 99999-4321 
# • Nome: "Pedro" 
#     Telefone: 99999-5678 
# Acesse o nome do primeiro contato e o telefone do segundo contato da agenda, 
# utilizando indexação adequada para tuplas aninhadas.

agenda = (("João", "99999-1234"), ("Maria", "99999-4321"), ("Pedro", "99999-5678"))
nome = agenda[0][0]
telefone = agenda[1][1]

print(f"Nome do primeiro contato: {nome}, telefone do segundo contato: {telefone}")