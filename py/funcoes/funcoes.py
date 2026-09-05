# **Funções**

# São blocos de código que executam funcionalidades específicas.
# Normalmente são utilizados para evitar que determinada parte do seu 
# código sejá escrito varias vezes.
# Em Python sua sintaxe é definida usando ***def*** e atribuindo um nome a ela, veja um exemplo:

def funcao():
    print("Bloco de código")


# Observando essa função, podemos extrair algumas informações, 
# iniciando com a palavra reservada para funções ***def*** o nome atribuido à função 
# funcao e os parênteses **( )** utilizado para definição dos dados de entrada da função, 
# também chamados de parâmetros.

# Em seguida usa-se dois pontos : e abaixo o bloco de código a ser executado, 
# que neste caso é apenas imprimir de uma string.

# Para “chamar” uma função, utilizamos o nome que foi definido, dessa forma:
def funcao():
    print("Bloco de código")
    
funcao()

print("-"*30)

# **Parâmetros**

# Além de executar código, funções também podem receber e retornar dados.
# Podemos enviar dados para uma função através de seus parâmetros.
# Observe o exemplo:

def imprime_nome(nome):
    print(f"Nome: {nome}")

imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")

print("-"*30)

# *Quando* a função é chamada, passamos uma string como dado de entrada - 
# através do parâmetro nome - que é concatenada e impressa dentro da função.
# Caso nenhum valor seja infomado ao chamar a função, um erro será gerado. 
# Por exemplo, o seguinte código:Quando a função é chamada, passamos uma string como dado de entrada
# - através do parâmetro nome - que é concatenada e impressa dentro da função.
# Caso nenhum valor seja infomado ao chamar a função, um erro será gerado. 
# Por exemplo, o seguinte código:

def imprime_nome(nome):
    print(f"Nome: {nome}")

# imprime_nome() # --> Isso Gera Erro

# **Valores Padrão (ou Valores Default)**

print("-"*30)

# A utilização dos valores padrão serve para dar um valor quando quem chamou a função não 
# passar nenhum valor para os parâmetros definidos.
# Fazemos isso dessa forma:

def flor(flor = "Rosa", cor = "Vermelha"):
    print(f"A cor da {flor} é {cor}")
    
flor()
flor("Orquídea", "Azul")

print("-"*30)

# **Chamada de Função Posicional versus Chamada de Função Nomeada**
# Quando chamamos uma função, podemos utilizar a localização dos parâmetros para fazer o
# casamento entre o que foi chamado e o que foi definido na função.
# Para entender melhor, veja o exemplo a seguir:
def monta_computador(cpu = "", armazenamento = 0, memoria = 0):
    print(f"A configuração é: \n\t- CPU: {cpu}\n\t- Armazenamento: {armazenamento}tb\n\t- Memória: {memoria}")

monta_computador("Intel Core i9", 4, 64)

print("-"*30)

# O programador que escreveu a chamada da função monta_computador está respeitando a posição dos parâmetros, ou seja:
# O valor** "Intel Core i9"** é referente ao primeiro parâmetro (cpu) O valor 4 é referente ao segundo parâmetro (armazenamento) O valor 64 se refere ao terceiro parâmetro (memoria)
# Essa é uma chamada de função posicional, ou seja: que respeita a ordem dos parâmetros.
# Outra forma de fazer essa chamada de função é utilizar os nomes dos parâmetros!
# Dessa forma, não é necessário respeitar a ordem de definição dos parâmetros!
# Veja o mesmo exemplo, mas agora utilizando os nomes dos parâmetros:

monta_computador(memoria=64,armazenamento=4, cpu='Intel Core i9')

print("-"*30)

# A saida será a mesma, pois como utilizamos os nomes, o Python saberá qual o valor 
# referencía cada paramêtro

# Parâmetro args
# Caso você queira desenvolver uma função que recebe um número variável de parâmetros, 
# você pode utilizar o parâmetro *args!
# Dessa forma, a função receberá os argumentos em forma de Tupla e você poderá 
# processá-los com um loop for por exemplo!
# Veja o código abaixo para entender melhor:

def maior_30(*args):
    print(args)
    print(type(args))

    for num in args:
        if num > 30:
            print(num)

maior_30(10, 20, 30, 40, 50, 60)

print("-"*30)


# O programador que escreveu a chamada da função monta_computador está respeitando a 
# posição dos parâmetros, ou seja:
# O valor** "Intel Core i9"** é referente ao primeiro parâmetro (cpu) O valor 4 é 
# referente ao segundo parâmetro (armazenamento) O valor 64 se refere ao 
# terceiro parâmetro (memoria)
# Essa é uma chamada de função posicional, ou seja: que respeita a ordem dos parâmetros.
# Outra forma de fazer essa chamada de função é utilizar os nomes dos parâmetros!
# Dessa forma, não é necessário respeitar a ordem de definição dos parâmetros!
# Veja o mesmo exemplo, mas agora utilizando os nomes dos parâmetros:

def dados_pessoais(**kwargs):
    print(type(kwargs))
    for chave,valor in kwargs.items():
        print(f"{chave}: {valor}")
    
dados_pessoais(nome = "João", idade = 35, carreira = "Desenvolvedor Fullstack")

print("-"*30)

# **Funções com retorno de dados**
# As funções também podem retornar valores através da palavra reservada return.
# Veja o exemplo:

def soma_dois_numeros(valor1, valor2):
    soma = valor1 + valor2
    return soma

valor_soma = soma_dois_numeros(32, 15)
print(valor_soma)
print(soma_dois_numeros(50, 10))

print("-"*30)

# **Funções com retorno múltiplos**
# Funções também podem retornar múltiplos dados. Veja o exemplo:
def soma_dois_numeros_e_calcula_media(valor1, valor2):
    soma = valor1 + valor2 
    media = (valor1 + valor2) / 2
    
    return soma, media

valor_soma = soma_dois_numeros_e_calcula_media(32, 15)
print(valor_soma)
print(soma_dois_numeros_e_calcula_media(50, 10))

print("-"*30)

# **Palavra reservada pass**

# Caso você deseje definir uma função sem corpo nenhum, 
# ou seja, sem código, saiba que isso irá disparar o erro ***IndentationError***, 
# pois funções não podem estar vazias.
# Porém se por algum motivo precisar use a palavra reservada **pass**, da seguinte forma:

# **Função de uma linha**
# Python possibilita a criação de funções com apenas uma linha de código. 
# Veja os exemplo a seguir:

def soma(valor1, valor2): return valor1 + valor2
def divisao(valor1, valor2): return valor1 // valor2
def multiplicacao(valor1, valor2): return valor1 * valor2

# Chamada das funções
print(soma(1, 5))
print(divisao(8,2))
print(multiplicacao(8, 2))