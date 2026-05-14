import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Africa Population Dashboard",
    page_icon="🌍",
    layout="wide" # Compatible mobile et écran large
)

# 2. CHARGEMENT DES DONNÉES (Optimisé avec Cache < 5s)
@st.cache_data
def load_data():
    df = pd.read_csv('africa_population_cleaned.csv')
    return df

df = load_data()
st.write(df.columns.tolist())

# Cette ligne affichera les noms de colonnes sur ton dashboard
# --- SIDEBAR - FILTRES INTERACTIFS ---
st.sidebar.header("🔍 Filtres de recherche")

# On définit les noms de colonnes pour éviter les KeyError
# Vérifie dans l'affichage de l'étape 1 si ces noms sont exacts
COL_PAYS = 'Country Name' 
COL_REGION = 'region'

# Filtre par Région
regions = df[COL_REGION].unique().tolist()
selected_region = st.sidebar.multiselect("Choisir une région", regions, default=regions)

# Filtre par Pays (dynamique)
# On vérifie si la colonne existe avant de filtrer
available_countries = df[df[COL_REGION].isin(selected_region)][COL_PAYS].unique().tolist()
selected_countries = st.sidebar.multiselect("Choisir les pays", available_countries, default=available_countries[:5])

# Filtre par Année (Slider)
min_year, max_year = int(df['year'].min()), int(df['year'].max())
selected_years = st.sidebar.slider("Période d'analyse", min_year, max_year, (2000, max_year))

# Application des filtres
df_filtered = df[
    (df['region'].isin(selected_region)) & 
    (df['Country Name'].isin(selected_countries)) &
    (df['year'].between(selected_years[0], selected_years[1]))
]

# 4. TITRE ET DESCRIPTION
st.title("🌍 Analyse de la Croissance Démographique en Afrique")
st.markdown(f"""
Ce dashboard explore l'évolution de la population africaine de {min_year} à {max_year}. 
Il permet de comparer les croissances régionales et d'identifier les tendances démographiques majeures.
""")

# 5. SECTION 1 : VUE D'ENSEMBLE (KPIs)
st.header("📌 Indicateurs Clés (KPIs)")
kpi1, kpi2, kpi3 = st.columns(3)

# Calculs pour les KPIs
latest_pop = df_filtered[df_filtered['year'] == selected_years[1]]['population'].sum()
avg_growth = df_filtered['growth_rate'].mean()
total_countries = df_filtered['Country Name'].nunique()

kpi1.metric("Population Totale (Sélection)", f"{latest_pop/1e6:.2f} M", help="Somme de la population des pays sélectionnés pour l'année max.")
kpi2.metric("Taux de Croissance Moyen", f"{avg_growth:.2f} %", delta_color="normal")
kpi3.metric("Nombre de Pays", total_countries)

st.divider()

# 6. SECTION 2 : ANALYSE TEMPORELLE (Graphique en ligne)
st.header("📈 Évolution Temporelle")
fig_line = px.line(
    df_filtered, 
    x="year", 
    y="population", 
    color="Country Name",
    title="Courbe de croissance de la population par pays",
    labels={"year": "Année", "population": "Nombre d'habitants", "Country Name": "Pays"}
)
st.plotly_chart(fig_line, use_container_width=True)
st.info("Description : Ce graphique montre la progression linéaire de la population. On observe souvent une accélération après les années 2000.")

# 7. SECTION 3 : COMPARAISON GÉOGRAPHIQUE (Carte Choroplèthe)
st.header("🗺️ Cartographie de la Population")
# On prend la dernière année sélectionnée pour la carte
df_map = df_filtered[df_filtered['year'] == selected_years[1]]
fig_map = px.choropleth(
    df_map,
    locations="Country Code",
    color="population",
    hover_name="Country Name",
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f"Densité de population en {selected_years[1]}",
    scope="africa"
)
st.plotly_chart(fig_map, use_container_width=True)

# 8. SECTION 4 : CORRÉLATIONS (Heatmap)
st.header("🔍 Analyse des Corrélations")
col_corr1, col_corr2 = st.columns([2, 1])

with col_corr1:
    corr = df_filtered[['year', 'population', 'growth_rate', 'pop_millions']].corr()
    fig_heat = px.imshow(corr, text_auto=True, aspect="auto", title="Matrice de corrélation (Variables numériques)")
    st.plotly_chart(fig_heat)

with col_corr2:
    st.write("🔎 **Insight :**")
    st.write("Une corrélation proche de 1 entre 'year' et 'population' indique une croissance démographique constante et ininterrompue sur la période.")

# 9. SECTION 5 : DISTRIBUTION (Box Plot)
st.header("📊 Distribution et Disparités")
fig_box = px.box(
    df_filtered, 
    x="region", 
    y="growth_rate", 
    color="region",
    title="Distribution du taux de croissance par région"
)
st.plotly_chart(fig_box, use_container_width=True)
st.info("Le Box Plot permet de voir les écarts de croissance au sein d'une même région. Les points isolés sont des pays atypiques.")

# BAS DE PAGE
st.divider()
st.caption("Données sources : Banque Mondiale (World Bank Open Data) | Réalisation : TANDAH DJIMELI MARCELLE - ASPIRING SENIOR DATA ANALYST")