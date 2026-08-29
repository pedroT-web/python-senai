# Imutáveis: Crie uma tupla chamada frutas contendo as frutas "maçã", "banana" e "laranja". 
# Tente alterar o valor da primeira fruta para "pera". 
# Explique por que essa operação não é possível e demonstre como criar uma nova tupla com a 
# alteração desejada.
frutas = ("Maçã", "Banana", "Laranja")

# frutas.remove("Maçã")
# frutas.insert(0, "Pera")
# print(frutas)

print("Isso não vai funcionar, pois uma tupla é Imutável, ela não aceita alterações após a criação da mesma, o que podemos fazer é recriar a tupla.")

frutas = ("Pera", "Banana", "Laranja")
print(frutas)
