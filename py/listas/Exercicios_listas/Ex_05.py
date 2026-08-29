# Combinar Duas Listas:
# Crie uma função que combine duas listas em uma única lista, intercalando seus
# elementos.

# Função que recebe duas listas como parâmetro
def intercalar_listas(l1, l2):
    # Lista vazia onde os elementos intercalados serão guardados
    resultado = []

    # zip() junta os elementos das duas listas em pares
    # Exemplo: [1, 3, 5] e [2, 4, 6] viram (1, 2), (3, 4), (5, 6)
    for a, b in zip(l1, l2):
        # Adiciona o elemento da primeira lista
        resultado.append(a)

        # Adiciona o elemento da segunda lista
        resultado.append(b)

    # Retorna a lista final com os elementos intercalados
    return resultado


# Primeira lista
lista_a = [1, 3, 5]

# Segunda lista
lista_b = [2, 4, 6]

# Chama a função e mostra o resultado na tela
print(f"Lista intercalada: {intercalar_listas(lista_a, lista_b)}")