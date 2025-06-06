import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel Programa em Rede", layout="wide")

st.title("📊 Painel Interativo – Programa em Rede dos Núcleos de Inovação Tecnológica do Estado")

# Carregar base
@st.cache_data
def load_data():
    return pd.read_csv("data/atividades_tratadas.csv")

df = load_data()

# Filtros
st.sidebar.header("Filtros")
eixo_sel = st.sidebar.multiselect("Eixo Estratégico", sorted(df["Eixo"].dropna().unique()))
tipo_sel = st.sidebar.multiselect("Categoria", sorted(df["Categoria"].dropna().unique()))
particip_sel = st.sidebar.text_input("Buscar participante")

df_filtrado = df.copy()

if eixo_sel:
    df_filtrado = df_filtrado[df_filtrado["Eixo"].isin(eixo_sel)]

if tipo_sel:
    df_filtrado = df_filtrado[df_filtrado["Categoria"].isin(tipo_sel)]

if particip_sel:
    df_filtrado = df_filtrado[df_filtrado["Participantes"].str.contains(particip_sel, case=False, na=False)]

# Layout
st.markdown("### 📈 Visão Geral dos Dados")

col1, col2 = st.columns(2)

with col1:
    fig_eixo = px.histogram(df_filtrado, x="Eixo", color="Eixo", title="Distribuição por Eixo Estratégico")
    st.plotly_chart(fig_eixo, use_container_width=True)

with col2:
    fig_cat = px.histogram(df_filtrado, x="Categoria", color="Categoria", title="Distribuição por Categoria (Tipo de Atividade)")
    st.plotly_chart(fig_cat, use_container_width=True)

st.markdown("---")
st.markdown("### 📋 Tabela de Atividades Filtradas")

st.dataframe(df_filtrado, use_container_width=True)

# Botões de exportação
st.download_button("📥 Baixar Excel", data=df_filtrado.to_csv(index=False), file_name="relatorio_programa_em_rede.csv", mime="text/csv")
