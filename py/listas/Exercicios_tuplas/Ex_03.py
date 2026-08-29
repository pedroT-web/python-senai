# Cidades: Crie uma tupla chamada cidades contendo as cidades "São Paulo", "Rio de Janeiro", 
# "Belo Horizonte" e "Salvador". Crie uma nova tupla chamada cidades_sul contendo apenas as cidades 
# "Rio de Janeiro" e "Belo Horizonte", utilizando fatiamento. 
# Crie outra tupla chamada pares contendo apenas os números pares da tupla numeros (1, 3 e 5), 
# utilizando fatiamento com passo.

cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador")
cidades_sul = (cidades[1], cidades[2])
print("As cidades selecionadas são: ", cidades_sul)

numeros = (1, 2, 3, 4, 5)
pares = numeros[1::2]
print(f"Os números pares são: {pares}")