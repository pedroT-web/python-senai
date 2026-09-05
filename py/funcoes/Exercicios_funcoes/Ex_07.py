# Tabuada:
# Crie uma função que receba um número inteiro como parâmetro e imprima a sua tabuada de 
# multiplicação completa.

def tabuada(num):
    i = 1
    while i <= 10:
        calculo = i * num
        print(f"{num} X {i} = {calculo}")
        
        i += 1

tabuada(6)