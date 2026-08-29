# Converter uma Lista em uma String e Vice-versa:
# Crie funções para converter uma lista em uma string separada por vírgulas e vice-versa.

lista = ["Python", "Java", "C#", "C++"]
string_lista = ",".join(lista)

texto = "Python, Java, C#, C++"
linguagens_lista = texto.split(",")

print(f"String: {string_lista}")
print(f"Lista: {linguagens_lista}")
