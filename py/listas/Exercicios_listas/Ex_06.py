# Verificar se um Elemento Está Presente em uma Lista:
# Implemente um programa que verifique se um determinado elemento está presente em
# uma lista.

lista_elementos = ["Elemento1", "Elemento2", "Elemento3"]

elemento = input("Digite o elemento que busca: ")
if elemento in lista_elementos:
    print("Este elemento esta presente na lista")
else:
    print("Este elemento não está na lista")