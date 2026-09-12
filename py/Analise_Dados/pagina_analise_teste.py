import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="DataPulse | Análise de dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


def gerar_dados(periodos: int, variacao: float, semente: int) -> pd.DataFrame:
    """Cria duas séries temporais com tendência e ruído controlável."""
    gerador = np.random.default_rng(semente)
    datas = pd.date_range(end=pd.Timestamp.today().normalize(), periods=periodos, freq="D")
    tendencia = np.linspace(20, 48, periodos)
    serie_a = tendencia + gerador.normal(0, variacao, periodos).cumsum() * 0.35
    serie_b = tendencia * 0.72 + 7 + gerador.normal(0, variacao, periodos).cumsum() * 0.3
    return pd.DataFrame({"Data": datas, "Série A": serie_a.round(2), "Série B": serie_b.round(2)})


def formatar_variacao(valor: float) -> str:
    return f"{'+' if valor >= 0 else ''}{valor:.1f}%"


with st.sidebar:
    st.title("📈 DataPulse")
    st.caption("Painel de exploração de dados")
    st.divider()
    nome = st.text_input("Seu nome", placeholder="Ex.: Ana")
    periodos = st.slider("Período analisado", 14, 180, 60, 7)
    variacao = st.slider("Nível de variação", 0.5, 8.0, 2.5, 0.5)
    semente = st.number_input("Semente dos dados", min_value=0, max_value=9999, value=42)
    tipo_grafico = st.radio("Visualização", ["Linha", "Área", "Barras"], horizontal=True)
    st.divider()
    st.caption("Ajuste os controles para explorar novos cenários.")

dados = gerar_dados(periodos, variacao, int(semente))
series_disponiveis = ["Série A", "Série B"]

st.title("📊 Visão geral de desempenho")
saudacao = f"Olá, **{nome}**! " if nome else ""
st.markdown(f"{saudacao}Acompanhe tendências, compare séries e exporte seus resultados em um só lugar.")
st.divider()

ultimo_a, anterior_a = dados["Série A"].iloc[-1], dados["Série A"].iloc[-2]
ultimo_b, anterior_b = dados["Série B"].iloc[-1], dados["Série B"].iloc[-2]
delta_a = (ultimo_a / anterior_a - 1) * 100
delta_b = (ultimo_b / anterior_b - 1) * 100

metricas = st.columns(4)
metricas[0].metric("Série A — último valor", f"{ultimo_a:,.1f}", formatar_variacao(delta_a))
metricas[1].metric("Série B — último valor", f"{ultimo_b:,.1f}", formatar_variacao(delta_b))
metricas[2].metric("Média do período", f"{dados[series_disponiveis].to_numpy().mean():,.1f}")
metricas[3].metric("Maior registro", f"{dados[series_disponiveis].to_numpy().max():,.1f}")

st.markdown("#### Evolução no período")
esquerda, direita = st.columns([3, 1])
with direita:
    series_selecionadas = st.multiselect("Séries exibidas", series_disponiveis, default=series_disponiveis)
    media_movel = st.checkbox("Exibir média móvel (7 dias)", value=True)

with esquerda:
    if not series_selecionadas:
        st.info("Selecione ao menos uma série para visualizar o gráfico.")
    else:
        grafico = dados.set_index("Data")[series_selecionadas]
        if media_movel:
            for serie in series_selecionadas:
                grafico[f"{serie} · média móvel"] = grafico[serie].rolling(7, min_periods=1).mean()
        if tipo_grafico == "Área":
            st.area_chart(grafico, use_container_width=True, height=360)
        elif tipo_grafico == "Barras":
            st.bar_chart(grafico, use_container_width=True, height=360)
        else:
            st.line_chart(grafico, use_container_width=True, height=360)

aba_dados, aba_insights = st.tabs(["Dados detalhados", "Insights rápidos"])
with aba_dados:
    tabela = dados.copy()
    tabela["Diferença A × B"] = (tabela["Série A"] - tabela["Série B"]).round(2)
    st.dataframe(tabela, use_container_width=True, hide_index=True, height=290)
    st.download_button("⬇️ Baixar dados em CSV", tabela.to_csv(index=False).encode("utf-8"), "datapulse_analise.csv", "text/csv")

with aba_insights:
    melhor_serie = dados[series_disponiveis].iloc[-1].idxmax()
    correlacao = dados["Série A"].corr(dados["Série B"])
    maior_data = dados.loc[dados[series_disponiveis].max(axis=1).idxmax(), "Data"].strftime("%d/%m/%Y")
    ins1, ins2, ins3 = st.columns(3)
    ins1.info(f"**Melhor resultado atual**\n\n{melhor_serie} lidera no último registro.")
    ins2.success(f"**Correlação entre séries**\n\n{correlacao:.2f} — elas se movem de forma semelhante.")
    ins3.warning(f"**Pico do período**\n\nO maior valor foi registrado em {maior_data}.")

st.caption("DataPulse · dados simulados para fins de demonstração")
