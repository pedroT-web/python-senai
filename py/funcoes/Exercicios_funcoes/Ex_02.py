# Maior número:
# Crie uma função que receba dois números como parâmetros e retorne o maior deles.

def maior(num1, num2):
    if num1 > num2:
        print(f"O maior número entre {num1, num2} é o {num1}")
    elif num2 > num1:
        print(f"O maior número entre {num1, num2} é o {num2}")
    else:
        print("Os números são iguais")
        
maior(30, 30)
 