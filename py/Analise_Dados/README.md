# PANDAS

## 1. O que é Pandas?
O Pandas é uma biblioteca do Python usada principalmente para trabalhar com dados em tabelas.
Imagine uma planilha do Excel:

nome  | idade | cidade | vendas
João  | 18    | SP     | 1500
Maria | 20    | RJ     | 2300
Pedro | 19    | MG     | 1800

### O Pandas permite fazer coisas como:

- criar tabelas;
- filtrar informações;
- ordenar;
- calcular médias;
- somar valores;
- agrupar dados;
- encontrar valores maiores/menores;
- limpar dados;
- analisar vendas;
- importar Excel/CSV;
- exportar resultados.

A estrutura principal é o DataFrame.

## 2. Importando o Pandas
```py
import pandas as pd
```
"pd" é o apelido

```py
pd.DataFrame()
```
Aqui estamos usando o DataFrame do Pandas.

## 3. O que é um DataFrame?
Pense como uma PLANILHA DENTRO DO PYTHON

```py
import pandas as pd

dados = {
    "nome": ["João", "Maria", "Pedro"],
    "idade": [18, 20, 19],
    "nota": [8.5, 9.0, 7.5]
}

df = pd.DataFrame(dados)

print(df)
```
df é a nossa "tabela"

Resultado:
```
    nome  idade  nota
0   João     18   8.5
1  Maria     20   9.0
2  Pedro     19   7.5
```

# 4. Índice
```
0
1
2
```
Esse é o índice das linhas.
Por padrão, o Pandas começa em 0.
```
0 → João
1 → Maria
2 → Pedro
```

# 5. Acessando uma coluna
Pegando somente os nomes
```py
print(df["nome"])
```
Saida:
```
0     João
1    Maria
2    Pedro
```

OU
```py
print(df.nome)
```

# 6. Acessando várias colunas
```py
print(df[["nome", "nota"]])
```
Saída:
```py
    nome  nota
0   João   8.5
1  Maria   9.0
2  Pedro   7.5
```

# 7. head() — primeiras linhas
```py
print(df.head())
```
Mostra as primeiras 5 linhas.

Primeiras 10:
```py
print(df.head(10))
```

# 8. tail() — últimas linhas
```py
print(df.tail())
```
Últimas 5 linhas.


```py
print(df.tail(10))
```

# 


🐼 AULÃO DE PANDAS — DO ZERO À ANÁLISE DE DADOS
1. O que é Pandas?

O Pandas é uma biblioteca do Python usada principalmente para trabalhar com dados em tabelas.

Imagine uma planilha do Excel:

nome	idade	cidade	vendas
João	18	SP	1500
Maria	20	RJ	2300
Pedro	19	MG	1800

O Pandas permite fazer coisas como:

criar tabelas;
filtrar informações;
ordenar;
calcular médias;
somar valores;
agrupar dados;
encontrar valores maiores/menores;
limpar dados;
analisar vendas;
importar Excel/CSV;
exportar resultados.

A estrutura principal que você vai usar é o DataFrame.

2. Importando o Pandas

Normalmente começamos assim:

import pandas as pd

O pd é apenas um apelido.

Então:

pd.DataFrame()

significa que estamos usando o DataFrame do Pandas.

3. O que é um DataFrame?

Pense nele como uma planilha dentro do Python.

import pandas as pd

dados = {
    "nome": ["João", "Maria", "Pedro"],
    "idade": [18, 20, 19],
    "nota": [8.5, 9.0, 7.5]
}

df = pd.DataFrame(dados)

print(df)

Resultado:

    nome  idade  nota
0   João     18   8.5
1  Maria     20   9.0
2  Pedro     19   7.5

O df é nossa tabela.

4. Índice

Observe o:

0
1
2

Esse é o índice das linhas.

Por padrão, o Pandas começa em 0.

Então:

0 → João
1 → Maria
2 → Pedro
5. Acessando uma coluna

Se quisermos somente os nomes:

print(df["nome"])

Resultado:

0     João
1    Maria
2    Pedro

Você também pode usar:

print(df.nome)

Mas eu recomendo:

df["nome"]

porque funciona melhor com nomes de colunas mais complexos.

6. Acessando várias colunas
print(df[["nome", "nota"]])

Resultado:

    nome  nota
0   João   8.5
1  Maria   9.0
2  Pedro   7.5

Perceba que usamos duas listas:

df[["nome", "nota"]]
7. head() — primeiras linhas

Muito importante.

print(df.head())

Mostra as primeiras 5 linhas.

Você também pode escolher:

print(df.head(10))

Primeiras 10.

8. tail() — últimas linhas
print(df.tail())

Últimas 5 linhas.

Ou:

print(df.tail(10))

Últimas 10.

9. shape

Quer saber quantas linhas e colunas existem?

print(df.shape)

Pode retornar:

(100, 5)

Significa:

100 linhas e 5 colunas.

10. columns

Mostra o nome das colunas:

print(df.columns)
11. info()

Uma das funções mais importantes para análise.

df.info()

Ela mostra:

quantidade de linhas;
nome das colunas;
valores não nulos;
tipo de cada coluna.

Por exemplo:

RangeIndex: 100 entries
Data columns:
nome       100 non-null object
idade      100 non-null int64
nota       98 non-null float64

Aqui descobrimos, por exemplo, que existem 2 notas faltando.

12. describe()

Outra função extremamente importante:

print(df.describe())

Ela gera estatísticas numéricas:

             idade       nota
count    100.000000  98.000000
mean      19.500000   8.120000
std        1.500000   0.800000
min       17.000000   5.000000
25%       18.000000   7.500000
50%       19.000000   8.200000
75%       21.000000   8.800000
max       24.000000  10.000000

Você pode interpretar:

count → quantidade
mean → média
min → menor
max → maior
50% → mediana
13. Filtrando dados

Agora começa a ficar realmente interessante.

Imagine:

df = pd.DataFrame({
    "nome": ["João", "Maria", "Pedro", "Ana"],
    "idade": [17, 20, 19, 25],
    "nota": [7, 9, 6, 10]
})

Quero apenas pessoas com nota maior que 7:

print(df[df["nota"] > 7])

Resultado:

    nome  idade  nota
0   João     17   7
1  Maria     20   9
3    Ana     25  10
14. Outros operadores

Você pode usar:

df[df["idade"] > 18]

Maior que 18.

df[df["idade"] < 18]

Menor que 18.

df[df["idade"] >= 18]

Maior ou igual.

df[df["idade"] <= 18]

Menor ou igual.

df[df["idade"] == 18]

Igual.

df[df["idade"] != 18]

Diferente.

15. Várias condições

Aqui é MUITO importante:

E → &

Quero pessoas com:

idade maior que 18
E nota maior que 7
df[(df["idade"] > 18) & (df["nota"] > 7)]
OU → |
df[(df["idade"] > 18) | (df["nota"] > 7)]

Significa:

idade maior que 18 OU nota maior que 7.

⚠️ No Pandas, não use:

and
or

para esse tipo de filtro.

Use:

&
|
16. loc

O loc é usado para selecionar dados usando rótulos/condições.

Por exemplo:

print(df.loc[df["nota"] > 7])

Também podemos escolher colunas:

print(df.loc[df["nota"] > 7, ["nome", "nota"]])
17. iloc

O iloc trabalha principalmente com posição.

print(df.iloc[0])

Primeira linha.

print(df.iloc[0:3])

Primeiras três linhas.

E:

print(df.iloc[:, 0])

Todas as linhas da primeira coluna.

18. Ordenando dados

Quer ordenar pela nota?

df.sort_values(by="nota")

Do menor para o maior.

Para fazer do maior para o menor:

df.sort_values(by="nota", ascending=False)

Isso é exatamente o que você fez no seu código:

resumo_dispositivo.sort_values(
    by="total_faturado",
    ascending=False
)

Ou seja:

Ordene pelo total_faturado, do maior para o menor.

19. sort_values() não modifica necessariamente o DataFrame

Você pode fazer:

df = df.sort_values(by="nota", ascending=False)

Assim você guarda o resultado.

Ou:

print(df.sort_values(by="nota", ascending=False))
20. Calculando média
print(df["nota"].mean())

Média.

21. Soma
print(df["nota"].sum())
22. Maior valor
print(df["nota"].max())
23. Menor valor
print(df["nota"].min())
24. Mediana
print(df["nota"].median())
25. Contagem
print(df["nota"].count())

Conta valores não vazios.

26. Valores únicos

Imagine:

df["cidade"]

Com:

SP
SP
RJ
MG
SP
RJ

Podemos descobrir quais cidades existem:

print(df["cidade"].unique())

Resultado:

["SP" "RJ" "MG"]
27. value_counts()

Esse é MUITO útil.

print(df["cidade"].value_counts())

Pode resultar:

SP    3
RJ    2
MG    1

Ou seja:

SP apareceu 3 vezes.

É muito usado para descobrir:

produto mais vendido;
cidade mais comum;
forma de pagamento mais utilizada;
status mais frequente;
dispositivo mais utilizado.
28. Trabalhando com dados faltantes

Imagine:

nome    idade
João    18
Maria   NaN
Pedro   20

NaN significa que o valor está ausente.

Podemos verificar:

print(df.isnull())

Ou:

print(df.isnull().sum())

Esse segundo é muito útil.

Ele pode mostrar:

nome     0
idade    1

Ou seja:

Existe 1 valor faltando em idade.

29. Removendo valores vazios
df = df.dropna()

Remove linhas que possuem valores vazios.

⚠️ Cuidado: isso pode apagar dados.

30. Preenchendo valores vazios

Por exemplo:

df["idade"] = df["idade"].fillna(0)

Ou podemos preencher com a média:

df["idade"] = df["idade"].fillna(df["idade"].mean())
31. Criando uma nova coluna

Isso é extremamente importante.

Imagine:

df["preco"]
df["quantidade"]

Podemos criar:

df["total"] = df["preco"] * df["quantidade"]

Agora temos:

preco    quantidade    total
10       3             30
20       2             40
15       5             75
32. Alterando uma coluna
df["preco"] = df["preco"] * 1.10

Aumenta todos os preços em 10%.

33. Renomeando colunas
df = df.rename(columns={
    "nome": "cliente",
    "idade": "idade_cliente"
})
34. Removendo coluna
df = df.drop(columns=["idade"])
35. Removendo linhas

Por índice:

df = df.drop(index=0)

Remove a linha 0.

36. Agrupamento — groupby()

Agora chegamos em uma das partes mais importantes do Pandas para análise de dados.

Imagine vendas:

dispositivo	faturamento
Celular	100
Computador	200
Celular	300
Tablet	150
Computador	400

Queremos saber quanto cada dispositivo faturou.

df.groupby("dispositivo")["faturamento"].sum()

Resultado:

Celular       400
Computador    600
Tablet        150

Isso significa:

Agrupe os dados por dispositivo e some o faturamento de cada grupo.

37. groupby() com várias estatísticas

É exatamente o que você estava fazendo.

resumo = df.groupby("dispositivo").agg(
    total_faturado=("faturamento", "sum"),
    media_itens=("quantidade", "mean"),
    pedidos=("transacao_id", "count")
)

Aqui estamos dizendo:

total_faturado
("faturamento", "sum")

Pegue faturamento e faça sum.

media_itens
("quantidade", "mean")

Pegue quantidade e calcule a média.

pedidos
("transacao_id", "count")

Conte quantas transações existem.

38. Por que usar reset_index()?

Depois de:

df.groupby("dispositivo")

o dispositivo pode virar o índice.

Então usamos:

.reset_index()

para transformar novamente em uma coluna normal.

E lembre:

.reset_index()

com ().

Sem:

.reset_index

você está pegando a função, e foi exatamente o erro que aconteceu no seu código.

39. agg() — agregação

O agg() permite fazer várias operações de uma vez.

Exemplo:

df.groupby("cidade").agg(
    vendas=("vendas", "sum"),
    media=("vendas", "mean"),
    maior=("vendas", "max"),
    menor=("vendas", "min"),
    quantidade=("vendas", "count")
)

Você consegue construir praticamente um relatório automático.

40. Filtrar + agrupar

Isso aparece MUITO em análise de dados.

No seu código:

df[df["status"] == "Concluído"]

Primeiro você pega apenas os pedidos concluídos.

Depois:

.groupby("dispositivo")

Agrupa por dispositivo.

Depois:

.agg(...)

Calcula as estatísticas.

Então seu código inteiro pode ser lido como:

Pegue apenas vendas concluídas → agrupe por dispositivo → calcule faturamento total, média de itens e quantidade de pedidos → transforme o índice em coluna.

Isso é a essência de muitas análises com Pandas.

41. Lendo CSV

Na vida real, você provavelmente não vai criar os dados manualmente.

Você vai receber arquivos.

Por exemplo:

df = pd.read_csv("vendas.csv")

E pronto: o CSV vira um DataFrame.

Depois:

print(df.head())
42. Lendo Excel
df = pd.read_excel("vendas.xlsx")
43. Salvando CSV

Depois de analisar:

df.to_csv("resultado.csv", index=False)

O:

index=False

evita salvar o índice do DataFrame como uma coluna extra.

44. Salvando Excel
df.to_excel("resultado.xlsx", index=False)
45. Uma análise completa

Imagine que temos:

import pandas as pd

df = pd.read_csv("vendas.csv")

Primeiro:

print(df.head())

Depois:

print(df.info())

Depois:

print(df.describe())

Verificamos valores vazios:

print(df.isnull().sum())

Filtramos vendas concluídas:

concluidos = df[df["status"] == "Concluído"]

Agrupamos:

resumo = concluidos.groupby("dispositivo").agg(
    faturamento=("faturamento_total", "sum"),
    media_itens=("quantidade", "mean"),
    pedidos=("transacao_id", "count")
).reset_index()

Ordenamos:

resumo = resumo.sort_values(
    by="faturamento",
    ascending=False
)

E mostramos:

print(resumo)

Isso já é uma análise de dados de verdade.

🧠 O mapa mental do Pandas

Se você decorar essa sequência, já vai conseguir fazer MUITA coisa:

               PANDAS
                  │
       ┌──────────┴──────────┐
       ↓                     ↓
    DataFrame              Series
       │
       ├── visualizar
       │    ├── head()
       │    ├── tail()
       │    ├── info()
       │    └── describe()
       │
       ├── selecionar
       │    ├── ["coluna"]
       │    ├── loc
       │    └── iloc
       │
       ├── filtrar
       │    ├── >
       │    ├── <
       │    ├── ==
       │    ├── &
       │    └── |
       │
       ├── calcular
       │    ├── sum()
       │    ├── mean()
       │    ├── median()
       │    ├── min()
       │    └── max()
       │
       ├── organizar
       │    ├── sort_values()
       │    ├── rename()
       │    └── drop()
       │
       ├── agrupar
       │    ├── groupby()
       │    └── agg()
       │
       ├── limpar
       │    ├── isnull()
       │    ├── dropna()
       │    └── fillna()
       │
       └── arquivos
            ├── read_csv()
            ├── read_excel()
            ├── to_csv()
            └── to_excel()
⭐ As 15 coisas que eu recomendo você decorar primeiro

Não tente decorar 100 funções. Comece por estas:

pd.DataFrame()
pd.read_csv()
df.head()
df.info()
df.describe()
df["coluna"]
df[condição]
df.loc[]
df.iloc[]
df.sort_values()
df.groupby()
df.agg()
df.isnull()
df.fillna()
df.dropna()

E principalmente, entenda a lógica, não só os comandos.

Por exemplo:

df[df["status"] == "Concluído"] \
    .groupby("dispositivo") \
    .agg(
        faturamento=("faturamento_total", "sum"),
        pedidos=("transacao_id", "count")
    ) \
    .reset_index() \
    .sort_values("faturamento", ascending=False)

Parece assustador no começo, mas você pode ler da esquerda para a direita:

Filtre → agrupe → calcule → organize → ordene.


