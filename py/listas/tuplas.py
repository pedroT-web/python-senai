# As Tuplas são sequências muito parecidas com listas, porém com algumas diferenças significativas:
# Sequência Imutável – conteúdo não pode ser modificado após ter sido criada.
# Útil para dados “fixos” (como uma espécie de sequência de constantes)
# Mais rápida que listas em algumas operações, como a iteração.
# Pode conter quaisquer tipos de dados, mesmo tipos diferentes na mesma tupla.
# As tuplas são usadas com frequência em funções que retornam valores múltiplos. Podemos pensar nas tuplas como se fossem uma espécie de lista de constantes.

# Como criar uma tupla em Python
# Criamos uma tupla usando parênteses ao atribuir os itens da coleção, separados por vírgulas, como segue:
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
print(halogenios)

print("="*30)

# As tuplas permitem a existência de itens duplicados entre seus elementos. Seus itens são indexados a partir de 0, como nas listas.
# O processo de criação de uma tupla também é chamado de “empacotamento” (“packing“).
# Podemos criar uma tupla contendo um único item se desejado. Para isso, devemos colocar uma vírgula após o item entre parênteses:
satelite_terra = ("Lua",)
print(type(satelite_terra))

print("="*30)

# Como as tuplas não são construídas para serem modificáveis, são mais simples e eficientes em 
# termos de uso de memória e performance, comparadas às listas.

# Tamanho de uma tupla
# Podemos descobrir o tamanho de uma tupla (número de elementos que a compõe) com a função len():
print(len(halogenios))

print("="*30)

# Como acessar os itens de uma tupla
# Podemos acessar elementos individuais na tupla usando colchetes e números de índice (como nas listas)
# Os elementos no final da lista podem ser acessados usando índices negativos, começando em -1 (da direita para a esquerda):
print(halogenios[-1])
print(halogenios[3])

print("="*30)

# Concatenação de tuplas Podemos concatenar (unir) duas ou mais tuplas em Python usando o operador de concatenação +
# Exemplo:
t1 = (5,7,8,6,9)
t2 = (7,12,3,0)
tc = t2 + t1
print(tc)
print(type(tc))

print("="*30)

# Observação: Não é possível concatenar tuplas com listas.

# Contar ocorrências em tuplas
# Podemos contar o número de ocorrências de um elemento em particular dentro de uma tupla com o método .count(), como segue:
t1 = (5,7,8,6,9,3,4,5,4,2,4)
print(t1.count(5))
print(t1.count(9))
print(t1.count(1))

print("="*30)

# Fatiamento de tuplas
# Podemos fatiar uma tupla – acessar um grupo sequencial de elementos de uma vez (operação de slicing):
print(halogenios[0:2])

print("="*30)

# Assim acessamos os elementos a partir do índice 0 até o índice 2, SEM incluir o elemento de índice 2. Se o índice inicial não for informado, é assumido automaticamente como 0:
print(halogenios[:3])

print("="*30)

# Se o índice final não for informado, é assumido como o final da tupla:
print(halogenios[0:])

print("="*30)

# Os últimos dois elementos da tupla:
print(halogenios[-2:])

print("="*30)

# Outras operações comuns com tuplas em Python
# Função len(): Informa o comprimento de uma tupla (ou outra sequência qualquer)
print(len(halogenios))

print("="*30)

# Operador in: retorna True se um elemento estiver na tupla, e False caso contrário.
print('Cl' in halogenios)
print('O' in halogenios)

print("="*30)

# Função sum(): retorna o somatório dos valores da tupla:
print(sum(t1))

print("="*30)

# Funções min() e max(): retornam os valores mínimo e máximo da tupla
print(min(t1))
print(max(t1))

print("="*30)

# Iteração sobre tuplas
# Podemos iterar sobre os elementos de uma tupla usando um laço for:
elementos = ('Ferro', 'Iodo', 'Ouro', 'Césio', 'Gálio')
for elemento in elementos:
    print('Elemento:', elemento)
    print('Aula de Química?')

# ou ainda:

for e in elementos: print(e)

print("="*30)

# Operações não disponíveis para tuplas
# Algumas operações disponíveis para listas para outras sequências não podem ser aplicadas sobre tuplas. Exemplos incluem:
# .sort() - este método classifica os elementos de uma lista em ordem crescente.
# .append() - este método adiciona um único elemento ao final da lista.
# .reverse() - Este método inverte a ordem dos elementos da lista.
# .remove() - Este método é usado para remover o primeiro elemento com um valor específico de uma lista.
# .pop() - Este método é usado para remover e retornar o último elemento de uma lista.
# pois estas são operações que efetuam alterações nos dados da sequência – e, como sabemos, as tuplas são imutáveis.

# Criar uma lista a partir de uma tupla
# Podemos criar uma lista a partir dos elementos presentes em uma tupla com a função list()
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
grupo17 = list(halogenios)
print(halogenios)
print(grupo17)
type(halogenios)
type(grupo17)

print("="*30)

# Criar uma tupla a partir de uma lista
# De forma inversa ao exemplo anterior, podemos também criar uma tupla com os elementos presentes em uma lista usando a função tuple()
halogenios = ['F', 'Cl', 'Br', 'I', 'At']
grupo17 = tuple(halogenios)
print(halogenios)
print(grupo17)
type(halogenios)
type(grupo17)