import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

# =========================================================
# 1. CONFIGURATION ET TITRE DE L'APPLICATION
# =========================================================
st.set_page_config(page_title="Mon Application Tout-en-Un", page_icon=":chart_with_upwards_trend:", layout="centered")

st.title("🚀 Mon Application Multi-Outils")
st.write("Bienvenue ! Découvre tes trois outils regroupés sur une seule et même page.")

st.markdown("---")

# =========================================================
# PROJET 1 : LE TABLEAU DE BORD (GRAPHIQUE INTERACTIF)
# =========================================================
st.subheader("📈 1. Évolution des données")

# Données d'exemple pour le graphique (de 2020 à 2026)
annees = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

donnees = pd.DataFrame({
    'Année': annees,
    'Produit A': [100, 120, 170, 210, 240, 280, 310],
    'Produit B': [80, 95, 110, 150, 190, 220, 250]
})

donnees_graphique = donnees.set_index('Année')
st.line_chart(donnees_graphique)

with st.expander("📊 Voir les données brutes"):
    st.dataframe(donnees)

st.markdown("---")

# =========================================================
# PROJET 2 : LE CHATBOT IA 💬
# =========================================================
st.subheader("💬 2. Assistant IA Intelligent")
st.write("Pose-moi tes questions ou discute avec moi !")

# Initialiser l'historique des messages s'il n'existe pas encore
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bonjour ! Je suis ton assistant virtuel. Que puis-je faire pour toi aujourd'hui ?"}
    ]

# Afficher les messages de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Zone de saisie pour l'utilisateur
if prompt := st.chat_input("Écris ton message ici..."):
    # Afficher le message de l'utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    # Génération d'une réponse
    with st.chat_message("assistant"):
        reponse = f"Je prends bien note de ton message : '{prompt}'. Notre connexion API complète arrive très vite pour te donner des réponses encore plus poussées !"
        st.write(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

st.markdown("---")

# =========================================================
# PROJET 3 : LE TRADUCTEUR AUTOMATIQUE 🌍
# =========================================================
st.subheader("🌍 3. Traducteur Instantané")
st.write("Saisis un texte et traduis-le instantanément dans la langue de ton choix !")

# Zone de saisie du texte
texte_a_traduire = st.text_area("Texte à traduire :", placeholder="Écris ou colle ton texte ici...")

# Sélection de la langue cible
langue_cible = st.selectbox(
    "Traduire en :",
    options=["Anglais", "Espagnol", "Allemand", "Italien", "Portugais", "Arabe", "Chinois"]
)

# Dictionnaire de correspondance pour le traducteur
langues_codes = {
    "Anglais": "en",
    "Espagnol": "es",
    "Allemand": "de",
    "Italien": "it",
    "Portugais": "pt",
    "Arabe": "ar",
    "Chinois": "zh-CN"
}

if st.button("Traduit maintenant ! 🚀"):
    if texte_a_traduire.strip() != "":
        try:
            # Traduction automatique
            code_langue = langues_codes[langue_cible]
            traduction = GoogleTranslator(source='auto', target=code_langue).translate(texte_a_traduire)
            
            # Affichage du résultat
            st.success("🎉 Traduction réussie :")
            st.write(traduction)
        except Exception as e:
            st.error("Oups, une erreur est survenue lors de la traduction.")
    else:
        st.warning("Dis-moi ce que je dois traduire d'abord ! 😉")

st.markdown("---")

# =========================================================
# 4. TES RÉSEAUX SOCIAUX
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
