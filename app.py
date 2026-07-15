import streamlit as st
import pandas as pd

# =========================================================
# 1. CONFIGURATION ET TITRE DE L'APPLICATION
# =========================================================
st.set_page_config(page_title="Mon Application", page_icon=":chart_with_upwards_trend:", layout="centered")
st.title("📈 Mon Tableau de Bord")
st.write("Bienvenue sur ton application ! Voici le suivi des données en temps réel.")

# =========================================================
# 2. LE TABLEAU DE BORD (GRAPHIQUE INTERACTIF)
# =========================================================
st.subheader("Évolution des données")

# Données d'exemple pour le graphique (de 2020 à 2026)
annees = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

donnees = pd.DataFrame({
    'Année': annees,
    'Produit A': [100, 120, 170, 210, 240, 280, 310],
    'Produit B': [80, 95, 110, 150, 190, 220, 250]
})

# On met l'année en index pour l'axe horizontal du graphique
donnees_graphique = donnees.set_index('Année')

# Affichage du graphique linéaire interactif
st.line_chart(donnees_graphique)

# Tableau déroulant pour voir les chiffres en détails
with st.expander("📊 Voir les données brutes"):
    st.dataframe(donnees)

# Ligne de séparation esthétique
st.markdown("---")

# =========================================================
# 3. TES RÉSEAUX SOCIAUX (100% OPÉRATIONNELS)
# =========================================================
st.write("### 📲 Rejoins la communauté !")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.link_button("✈️ Telegram", "https://t.me/Baptiste202420")
with col2:
    st.link_button("🐦 Twitter", "https://x.com/bbacri2")
with col3:
    st.link_button("📸 Instagram", "https://www.instagram.com/baptistebacri?")
with col4:
    st.link_button("🎵 TikTok", "https://www.tiktok.com/@bbenallou0?_r=1&_t=ZN-983TROLjC34")
with col5:
    st.link_button("💬 Discord", "https://discord.gg/FM7vXYRHS")
