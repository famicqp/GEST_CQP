import streamlit as st
import pandas as pd
from google.oauth2 import service_account

# Connexion aux données en temps réel
def get_data():
    # Ici, vous utilisez la librairie 'gspread' ou 'streamlit-gsheets'
    # pour lire votre fichier Google Sheets en direct
    df = st.connection("gsheets", type="google_sheets").read(worksheet="Suivi_Formations")
    return df

st.title("🚀 Pilotage CQP")

# Données synchronisées
data = get_data()

# Affichage avec alertes automatiques
st.subheader("Alertes prioritaires")
alertes = data[data['Statut'] == 'Urgent']
if not alertes.empty:
    st.error(f"Attention : {len(alertes)} dossiers nécessitent votre action immédiate")

# Formulaire de mise à jour rapide (Action)
with st.expander("Ajouter un commentaire ou une action"):
    comment = st.text_area("Note pour l'équipe :")
    if st.button("Envoyer la mise à jour"):
        # Logique pour écrire dans le Sheet
        st.success("Données synchronisées avec succès !")
