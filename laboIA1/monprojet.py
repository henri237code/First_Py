import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Analyse du Marché Immobilier Californien", layout="wide")

# Titre de l'application
st.title(" Analyse des facteurs influençant le prix des logements en Californie")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("data/housing.csv")

data = load_data()

# Afficher un aperçu des données
if st.checkbox("Afficher les 5 premières lignes des données"):
    st.write(data.head())

# Statistiques descriptives
st.subheader(" Statistiques descriptives")
st.write(data.describe())

# Distribution des prix
st.subheader("Distribution des prix")
fig, ax = plt.subplots(figsize=(6,4))  
sns.histplot(data['median_house_value'], kde=True, color='skyblue')
plt.xlabel('Prix médian des logements')
st.pyplot(fig)

# Heatmap des corrélations
st.subheader(" Corrélations entre les variables")
numeric_data = data.select_dtypes(include=[np.number])
fig2, ax2 = plt.subplots(figsize=(6,5))  # Taille réduite (avant c'était 10x8)
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
st.pyplot(fig2)

# Boxplot par rapport à la variable la plus influente (exemple : median_income)
st.subheader("  Prix vs Revenu Médian des Ménages")
fig3, ax3 = plt.subplots(figsize=(6,4))  # Taille réduite
sns.boxplot(x=pd.qcut(data['median_income'], q=4), y=data['median_house_value'])
plt.xticks(rotation=45)
plt.xlabel('Quartiles de Revenu Médian')
plt.ylabel('Prix Médian des Logements')
st.pyplot(fig3)

# Pairplot optionnel (long à calculer, à activer manuellement)
if st.checkbox("Afficher la matrice de pairplots (peut être long)"):
    st.subheader("Analyse détaillée : Pairplot")
    pairplot_fig = sns.pairplot(numeric_data, height=2.5)  # Hauteur plus petite par plot
    st.pyplot(pairplot_fig.fig)  # accéder à la figure matplotlib du pairplot

# Recommandations (à étoffer pour le rapport final)
st.subheader("Recommandations stratégiques")
st.write("""
- Les logements dans les zones à haut revenu médian se vendent nettement plus cher.
- La localisation géographique et la superficie sont également des facteurs déterminants.
- Les agences immobilières devraient concentrer leurs efforts sur les secteurs à revenus élevés et proposer des logements de plus grande surface pour maximiser leur rentabilité.
""")

# Pied de page
st.markdown("---")
