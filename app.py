import streamlit as st

st.title("📝 Générateur de Retour d'Expérience")

st.markdown("Remplis les champs ci-dessous pour générer ton paragraphe.")

chantier = st.text_input("Nom du chantier / projet")
objectif = st.text_input("Objectif principal du projet")
contexte = st.text_area("Contexte du projet (ex: transition écologique, innovation...)")
details_objectif = st.text_area("Objectifs précis du projet")
methode = st.text_area("Méthodologie utilisée (outils, analyses...)")
resultats = st.text_area("Résultats obtenus")
benefices = st.text_area("Bénéfices / limites")
conclusion = st.text_area("Conclusion & recommandations futures")

if st.button("Générer le texte"):
    st.markdown("---")
    st.subheader("✏️ Retour d'expérience généré :")
    st.write(f"""
    Dans le cadre de mon travail de fin d’études, j’ai mené un projet sur **{chantier}**, visant à **{objectif}**.
    Ce chantier s’inscrit dans un contexte de **{contexte}**.
    
    L’objectif principal était de **{details_objectif}**, afin d’optimiser certains aspects du projet.
    Pour cela, j’ai mis en place **{methode}**.
    
    Les résultats obtenus montrent que **{resultats}**. Ces données permettent d’identifier **{benefices}**.
    
    En conclusion, ce projet a permis **{conclusion}**.
    """)
