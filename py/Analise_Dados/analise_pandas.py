import pandas as pd
import numpy as np

# Criação de massa dados simulado vendas de Tecnologia /Iot
dados = {
    'transacao_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'dispositivo': ["Sensor A", "Medidor Smart", "Gatway", "Sensor A", "Medidor Smart", "Gateway", "Sensor B", "Sensor A"],
    'regiao': ["Sudeste", "Sul", "Sudeste", "Nordeste", "Sul", None, "Sudeste", "Nordeste"],
    'quantidade': [12, 5, 2, 8, np.nan, 3, 15, 7],
    'preco_unitario': [150.0, 420.0, 890.0, 150.0, 420.0, 890.0, 180.0, 150.0],
    'status': ["Concluído", "Pendente", "Concluído", "Cancelado", "Concluído", "Concluído", "Concluído", "Concluído"]
}

df = pd.DataFrame(dados)

print("Formato do DataFrame (Linhas, Colunas): ", df.shape)

print("==="*10)

# 1. Visão geral da estrutura e uso da memória
df.info()

print("==="*10)

# 2. Estatísticas descritivas de colunas numéricas
print(df.describe())

print("==="*10)

# 3. Contagem de valores ausentes por coluna
print("\nValores nulos por campo: ")
print(df.isnull().sum())

print("==="*10)

# Tratamento 1: Preenchimento de texto desconhecido
df['regiao'] = df['regiao'].fillna("Não Informada")

# Tratamento 2: Imputação da mediana em quantidade faltantes
mediana_qtd = df['quantidade'].median()

# Tratamento 3: Criação de coluna calculada (Engenharia de Recursos)
df['faturamento_total'] = df['quantidade'] * df['preco_unitario']

print(df.head())

print("==="*10)

# Vendas concluidas no Sudeste
filtro = (df["status"] == "Concluído") & (df["regiao"] == "Sudeste")
df_sudeste_concluido = df.loc[filtro, ["transacao_id", "dispositivo", "faturamento_total"]]
print(df_sudeste_concluido)

print("==="*10)

# Relatório por dispositivo: Total faturado e quantidade média por pedido
resumo_dispositivo = df[df['status'] == 'Concluído'].groupby("dispositivo").agg(
    total_faturado = ("faturamento_total", "sum"),
    media_itens = ("quantidade", "mean"),
    pedidos = ("transacao_id", "count")
).reset_index()

# Ordenação descendente pelo faturamento
resumo_dispositivo = resumo_dispositivo.sort_values(by="total_faturado", ascending=False)
print(resumo_dispositivo)

print("==="*10)

# Desafio Prático Proposto aos Alunos
# Peça aos alunos para responderem às seguintes perguntas usando apenas o DataFrame tratado:

# **Qual região gerou o maior volume financeiro em transações com status "Concluído"?**

regiao_maior_transacao = df[
    (df["status"] == "Concluído") & 
    (df["quantidade"] == df["quantidade"].max())]
print(regiao_maior_transacao)

print("==="*10)

# **Qual foi o ticket médio (faturamento total médio) de transações por região?**

faturamento_total_regiao = df.groupby("regiao")["preco_unitario"].mean()

print(faturamento_total_regiao)

# **Exporte o resultado da questão 1 para um arquivo CSV chamado faturamento_por_regiao.csv,
# sem incluir o índice numérico.
faturamento_total_regiao.to_csv("faturamento_por_regiao.csv", index=False)
