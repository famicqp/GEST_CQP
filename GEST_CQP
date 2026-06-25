import streamlit as st
import pandas as pd

# Configuration pour mobile
st.set_page_config(page_title="Direction CQP", layout="centered")

st.title("📱 Tableau de Bord")

# Simulation de données (à remplacer par la lecture de votre fichier Excel/Sheet)
data = {'Département': ['Bois', 'Alu', 'Élec. Ind', 'Élec. Bât'],
        'Taux_Occupation': [85, 90, 75, 95]}
df = pd.DataFrame(data)

# Affichage en carte (plus lisible sur petit écran)
for index, row in df.iterrows():
    with st.container(border=True):
        col1, col2 = st.columns([2, 1])
        col1.write(f"**{row['Département']}**")
        col2.metric(label="Taux", value=f"{row['Taux_Occupation']}%")

# Bouton d'action rapide pour le directeur
if st.button("Rafraîchir les données"):
    st.rerun()
