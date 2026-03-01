import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyse de Sentiment - Kappa", layout="wide")
st.title("📊 Dashboard - Analyse de Sentiment Temps Réel")
st.caption("Pipeline : NiFi → Kafka → Spark → Streamlit")

col1, col2, col3 = st.columns(3)
col1.metric("Total messages", 0)
col2.metric("😊 Positif", 0)
col3.metric("😠 Négatif", 0)

st.info("En attente de données Kafka... Vérifiez que le pipeline est lancé.")
