# Fatiar uma Lista:
# Crie um programa que demonstre como fatiar uma lista para obter sublistas.
lista = [10, 20, 30, 40, 50, 60]

metade = len(lista) // 2

lista1 = lista[:metade]
lista2 = lista[metade:]

print(lista1)
print(lista2)