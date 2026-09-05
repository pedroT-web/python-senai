# Classificador de triângulos:
# Crie uma função que receba os comprimentos dos lados de um triângulo como 
# parâmetros e retorne a sua classificação (equilátero, isósceles ou escaleno).

def triangulo(ladoa, ladob, ladoc):
    if ladoa == ladob and ladoa == ladoc:
        print("Este triângulo é equilátero")
    elif ladoa == ladob and ladoc != ladoa or ladoa == ladoc and ladob != ladoa:
        print("Este triângulo é isóceles")
    elif ladoa != ladob and ladoa != ladoc:
        print("Este triângulo é escaleno")
    else:
        print("Triangulo inválido")
        
triangulo(10, 10, 2)
        