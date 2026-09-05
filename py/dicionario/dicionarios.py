# Aula: Dicionários em Python
# Este material foi preparado com base nos conceitos da ementa oficial focado nas aplicações de programação. Contém 3 exemplos práticos para cada um dos 5 principais tópicos da aula, prontos para execução pelos alunos.
# 1. Criação e Sintaxe Básica
# Como criar um dicionário definindo chaves e valores associados.


# Exemplo 1.1: Dicionario sobre um time de futebol
time = {
    "time": "Palmeiras",
    "fundacao": "1920",
    "mundial": 0
}
print(time)

print("-"*30)

# Exemplo 1.2: Dicionario sobre o jogo em python(pygame)
jogo_retro = {
    "titulo": "River Raid",
    "estilo": "Aviação",
    "linguagem": "python"
}
print(jogo_retro)

print("-"*30)

# Exemplo 1.3: Dicionario de informações de um instrutor
instrutor = {
    "nome": "Café",
    "instituicao": "Senai",
    "unidade": "Sumaré"
}
print(instrutor)

print("-"*30)

## 2. Acessando Elementos (Chaves, Valores e Itens)
# Utilizando as funções internas `.keys()`, `.values()` e `.items()`.

# Exemplo 2.1: Acessando apenas os itens (.items())
comidas_favoritas = {
    "comida": "Lanche",
    "suco": "Laranja",
    "refrigerante": "Coca-Cola"
}
print("Para(Chave, Valor): ", comidas_favoritas.items())

print("-"*30)

# Exemplo 2.2: Acessando apenas os valores (.values())
certificacoes = {
    "cloud1": "AWS Cloud Practitioner",
    "cloud2": "Azure Data Fundamentos",
    "dev": "Python Essentials"
}
print("Lista de certificações: ", certificacoes.values())

print("-"*30)

# Exemplo 2.3: Acessando apenas as chaves (.keys())
familia = {
    "filha": "Julia",
    "sobrinho": "Daniel",
}
print("Parenesco mapeados: ", familia.keys())

print("-"*30)

# Exemplo 3.1: Exibindo itens formatados com f-string
comidas_favoritas = {
    "comidas": "Lanche",
    "suco": "Laranja",
    "refrigerante": "Coca-Cola"
}
for k,v in comidas_favoritas.items():
    print(f"O {k} favorito é {v}")
   
print("-"*30)
    
# Exemplo 3.2: Laço FOR sobre tecnologias de desenvolvimento
tecnologias = {
    "Linguagem": "Python",
    "Banco de dados": "MongoDB",
    "Deploy": "Azure"
}
for chave, valor in tecnologias.items():
    print(f"{chave} utilizada: {valor}")

print("-"*30)

# Exemplo 3.3: Iterando para processar relatórios.
relatorio = {
    "ZFA": 1500,
    "UtilityUIQ": 3200,
    "Sea3000": 850
}
total_mediadores = 0
for quantidade in relatorio.values():
    total_mediadores += quantidade
print(f"Total de mediadoes processados: {total_mediadores}")

# 4. Adicionando, Alterando e Removendo Itens
# Métodos para atualizar a estrutura de um dicionário existente.

# Exemplo 4.1: Adicionando e Alterando itens
comidas_favoritas = {
    "comida": "Lanche",
    "suco": "Laranja"
}

comidas_favoritas["sobremesa"] = "Torta Holandesa" # Adicionando
comidas_favoritas["suco"] = "Maracujá" # Alterando
print("Dicionário Atualizado:", comidas_favoritas)

# Exemplo 4.2: Manipulando o status de um projeto
projeto = {
    "nome": "SmartOferta",
    "status": "Desenvolvimento"
}
print("Antes: ", projeto)
projeto["status"] = "Produção" # Alterando
projeto["integracao"] = "Telegram" # Adicionando
print("Depois: ", projeto)

# Exemplo 4.3: Removendo itens com DEL
aluno = {
    "nome": "William",
    "curso": "Sistemas",
    "trancado": True
}
print("Com chave 'trancado': ", aluno)
del aluno["trancado"] # Deletando a chave
print("Após usar o del: ", aluno)

# 5. Dicionários do Zero e Listas
# Como criar dicionários vazios e inseri-los dentro de listas usando .copy().

# Exemplo 5.1: Criando estrutura a partir do zero
estado = {}
brasil = list()

# Simulando entrada de 2 estados
dados = [("São Paulo", "SP"), ("Minas Gerais", "MG")]

for nome,sigla in dados:
    estado['uf'] = nome 
    estado['sigla'] = sigla
    brasil.append(estado.copy()) # O .copy() é essencial para não sobrescrever

print(brasil)

# Exemplo 5.2: Iterando sobre uma lista de dicionários
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print() # Quebra de linha

# Exemplo 5.3: Lista de dicionários para turmas
turmas = []
curso1 = {"id": 1, "materia": "Microsoft AI", "alunos": 250}
curso2 = {"id": 2, "materia": "Python", "alunos": 250}

turmas.append(curso1.copy())
turmas.append(curso2.copy())

print("Estrutura final de turmas:", turmas)
