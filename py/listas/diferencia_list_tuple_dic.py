# Lista é uma coleção ordenada e MUTÁVEL. Permite membros duplicados
# Indice    0       1   2   3 
lista = ["carro", True, 2, 2.1]
print(lista)
print(lista[3])
print(type(lista))
print("="*30)

# Tupla é uma coleção ordenada e IMUTÁVEL. Permite membros duplicados
# Indice     0      1   2   3
tupla = ("Carro", True, 2, 2.1)
print(tupla)
print(tupla[3])
print(type(tupla))
print("="*30)

# Dicionário é uma coleção ordenada e MUTÁVEL. Não Permite membros duplicados
# Chave: Valor
dicionario = {"nome": "Carro", "logica": True, "numero": 2, "outroNumero": 3.5}
print(dicionario)
print(dicionario["nome"])
print(type(dicionario))
print("="*30)

# Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado
conjunto = {"carro", True, 2, 3.5} 
print(conjunto)
print(type(conjunto))
# print(conjunto[0]) -> Não consegue trazer pois não tem índice
