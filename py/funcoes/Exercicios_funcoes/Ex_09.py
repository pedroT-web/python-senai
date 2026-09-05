# Análise de texto:
# Crie uma função que receba um texto como parâmetro e retorne a quantidade de letras maiúsculas, 
# minúsculas e espaços presentes no texto.

def verificacao_texto(texto):
    maiusculas = []
    minusculas = []
    qtdMaiusculas = 0
    qtdMinusculas = 0
    qtdEspacos = 0
    for letra in texto:
        if letra.isupper():
            qtdMaiusculas += 1
            
            maiusculas.append(letra)
        if letra.islower():
            qtdMinusculas += 1
            
            minusculas.append(letra)    
        if letra.isspace():
            qtdEspacos += 1        
    print(f"A quantidade de letras maiúsculas é: {qtdMaiusculas}, sendo elas:  {maiusculas}")
    print(f"A quantidade de letras minúsculas é: {qtdMinusculas}, sendo elas:  {minusculas}")
    print(f"A quantidade de espaços vazios é: {qtdEspacos}")

verificacao_texto("OLA mundo")