# Verificação de idade:
# Crie uma função que receba a idade de uma pessoa como parâmetro e retorne 
# True se ela for maior de idade (18 anos) ou False caso contrário.

def maior_idade(idade):
    if idade >= 18:
        print(True)
        return True
    else:
        print(False)
        return False 

maior_idade(18)