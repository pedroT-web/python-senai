import streamlit as st
import pandas as pd
import numpy as np

# Título e Texto
st.title("Meu primeiro App com Streamlit")
st.write("Exemplo simples demonstrando widgets e renderização básica")

# Entrada de Texto
nome = st.text_input("Qual é o seu nome? ")

if nome:
    st.success(f"Olá, {nome}!")
# Slider para entrada númerica
pontos = st.slider("Quantidade de pontos do gráfico: ", min_value = 10, max_value = 100, value = 30)

# Geração de dados aleatórios e exibição em gráfico
dados = pd.DataFrame(
    np.random.randn(pontos,2),
    columns=["Serie A", "Serie B"]
)
st.subheader("Gráfico Interativo")
st.line_chart(dados)
