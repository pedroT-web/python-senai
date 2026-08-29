# LISTAS
# Uma Lista (list) em Python, nada mais é que uma coleção ordenada de valores, separados por vírgula e dentro de colchetes [].
# Elas são utilizadas para armazenar diversos itens em uma única variável. Entender este conteúdo é de extrema importância para dominar a linguagem por completo!
# Abaixo temos um exemplo de uma lista:

lista = ["PythonAcademy"]
print(lista)

print("="*30)


# Lista Vazia
lista_vazia = []
print(lista_vazia)

print("="*30)


# Podemos utilizar a função list do próprio python (built-in function)
lista = (["python Academy"])
print(lista)

print("="*30)

# Outra forma é criar lista resultante de uma operação de List Comprehensions!
# 1. Primeiro criamos a origem dos dados 
interavel = ["Notebook", "Mouse", "Monitor"]
# 2. Agora o python sabe de onde tirar o 'item'
novaLista = [item.upper() for item in interavel]

print(novaLista) # Saida: ['NOTEBOOK', 'MOUSE', 'MONITOR']

print("="*30)

# Podemos ainda criar lista através da função range(), dessa forma:
lista_10 = list(range(10))
print(lista_10)

print("="*30)

# Acessando dados da lista Todos os itens de uma lista são indexados, ou seja 
# para cada item da lista um indice é atribuido da seguinte forma: lista[indice]
fruta = ["Maçã", "Banana", "Jaca", "Melão", "Abacaxi"]

# Os indices são iniciados em 0, ou seja como podemos acessar o primeiro item da lista que é o indice 0?
print(fruta[0]) # Saída: Maçã
print(fruta[2]) # Saída: Jaca

print("="*30)

# Indexação Negativa
# O conceito de indexação negativa, que significa começar do fim, então -1 se refere ao último item. Por exemplo:
print(fruta[-3]) # Saída: Jaca

print("="*30)

# Lista dentro de lista
# Suponha que exista uma lista dentro de uma lista, assim:
lista = ['item1', ['python', 'academy'], 'item3']

# Como podemos acessar o primeiro indice do item que é uma lista?
# A resposta é simples, basta selecionar a posição em que se localiza a lista para ter acesso a ela, assim:
sublista = lista[1]
print(sublista[0])

print("="*30)

print(lista[1][0])

print("="*30)

# Lista [inicio: fim: passo]
lista = [10, 20, 30, 40, 50, 60]
print(lista[2:5]) # Saída -> [30, 40, 50]
print(lista[0::5]) # Saída -> [10, 60]

print("="*30)

#Com a função enumerate() podemos percorrer tambem o indice referente a cada valor da lista
for indice, valor in enumerate(lista):
    print(f"Indice: {indice}, valor = {valor}")


print("="*30)

# Que tal poupar algumas linhas de código e obter o mesmo resultado com o list comprehension?
[print (num)for num in lista] # Saída -> Todos os valores da lista

# Com enumerate
[print(f"Indice: {indice}, valor = {valor}") for indice, valor in enumerate(lista)] # Saida -> Indices e valores da lista

print("="*30)

# Comprimento de uma Lista
# O comprimento de uma lista, ou o número de itens que a compõem, pode ser obtido a partir da função len(), 
# como mostra o código abaixo, em que é impresso o valor 4, indicando que a variável qtdDEItens contém 4 elementos.

minhaLista = ["Python", "é", "muito", "bom"]
qtdItens = len(minhaLista)
print(qtdItens) # Saida -> 4

print("="*30)


# Acessar Elementos em uma Lista
# Para acessar um elemento de uma lista, são aplicados índices. 
# Eles são números inteiros que indicam a posição de um elemento em uma lista. 
# Para selecionar um elemento, especifique seu índice entre colchetes. 
# A indexação varia de 0 a n-1, onde n é o tamanho da lista. 
# Por exemplo, em uma lista com 3 elementos, os respectivos índices de cada um dos itens seriam 0, 1 e 2.
lista2 = ["um", 2, 3.14]
print(lista2[0]) # Saida: "um"
print(lista2[1]) # Saida: 2
print(lista2[2]) # Saida: 3.14

print("="*30)

# Negativo
print(lista2[-1]) # Saida: 3.14
print(lista2[-2]) # Saida: 2
print(lista2[-3]) # Saida: "um"

print("="*30)

# Métodos
# Os métodos de listas em Python são recursos que permitem manipular e trabalhar com listas de forma eficiente e poderosa. 
# Uma lista é uma estrutura de dados que armazena uma coleção de elementos, onde cada elemento é identificado por um índice. 
# Os métodos de listas fornecem funcionalidades para adicionar, remover, ordenar, pesquisar e realizar várias operações em listas.

# Principais Métodos de Listas

# **append()**
# **Append** significa incluir ou anexar. Este método adiciona um elemento no final da lista.

food = ["pasta", "pizza", "lasanha"]
food.append("macarrão")
print(food) # Saída -> ["pata", "pizza", "lasanha", "macarrão"]

print("="*30)

# **clear()**
# **Clear** significa limpar. Este método apaga todos os elementos de uma lista.
food.clear()
print(food) # Saida -> [] lista vazia (limpou a lista)

print("="*30)


# **copy()**
# **Copy** significa copiar. Este método retorna uma cópia da lista.copy()
# Copy significa copiar. Este método retorna uma cópia da lista.
food = ["pasta", "pizza", "lasanha"]
food2 = food.copy()
print(food2) # Saida: ["pata", "pizza", "lasanha"]

print("="*30)

# **count()**
# **Count** significa contar. Este método retorna o número de elementos que contenham o valor especificado.
x = food.count("pizza")
print(x) # Saida -> 1 quantidade de pizzas que tem na lista

print("="*30)

# **extend()**
# **Extend** significa estender. Este método adiciona os elementos de uma lista ao final de outra lista.
sobremesa = ["Chocolate", "Sorvete"]
food.extend(sobremesa)
print(food)

print("="*30)


# **index()**
# **Index** significa índice. Este método retorna a posição do primeiro elemento que contenha o valor especificado.
x = food.index("pizza")
print(x) # Saída -> 1 index do objeto pizza na lista food

print("="*30)

# insert()
# Insert significa inserir. Este método adiciona um elemento a uma posição específica.
food.insert(1, "spaghetti") # adicionou o spaghetti na posição 1
print(food) 

print("="*30)

# pop()
# Pop significa estourar. Este método remove um elemento de uma posição específica.

food.pop(1) # Remove o item na posição 1
print(food)

print("="*30)

# **remove()**
# **Remove** significa remover. Este método remove o primeiro item com o valor especificado.
food.remove("lasanha")
print(food)

print("="*30)

# *reverse()**
# **Reverse** significa reverter. Este método reverte a ordem da lista.
food.reverse()
print(food)

print("="*30)

# sort()
# Sort significa ordenar. Este método ordena a lista alfabeticamente.
food.sort()
print(food)