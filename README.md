#Africa Population Pulse : Dashboard Analytique Streamlit

#Présentation du Projet

Ce projet a été réalisé dans le cadre du Sprint S2 de mon stage Master 2 chez Formuloo.
L'objectif est de transformer des données brutes de la Banque Mondiale concernant la population des 54 pays d'Afrique (de 1960 à 2023) en un outil d'aide à la décision interactif et visuel.
Lien du Dashboard : link: https://dashboard-analytique-app-sur-dataset-population-africaine-xdh8.streamlit.app/

#Stack Technique

Langage : Python 3.12
Analyse de données : Pandas, NumPy
Visualisation : Plotly Express (Graphiques interactifs)
Interface : Streamlit
Déploiement : Streamlit Community Cloud

#Pipeline de Données (ETL)

Le projet suit une rigueur de traitement de donnée structurée :
Extraction : Récupération du dataset "World Development Indicators" de la Banque Mondiale.
Transformation (Wide to Long) : Transformation du format large (années en colonnes) vers un format long via la méthode melt. Le dataset est passé de 54 lignes à plus de 3 400 lignes.
Nettoyage & Enrichissement :
Normalisation des noms de colonnes (snake_case).
Traitement des valeurs manquantes par imputation à la médiane par pays.
Détection d'outliers via la méthode IQR (Écart Interquartile).
Création de 10 colonnes analytiques (Taux de croissance YoY, Population en millions, Régions, Décennies, etc.).
Chargement : Export en fichier CSV optimisé pour le dashboard.

#Fonctionnalités du Dashboard

Le dashboard propose 5 niveaux de lecture :
- Indicateurs Clés (KPIs) : Visualisation instantanée de la population totale filtrée et du taux de croissance moyen.
- Analyse Temporelle : Graphique en ligne montrant les trajectoires de croissance par pays.
- Comparaison Géographique : Carte choroplèthe interactive de l'Afrique.
- Matrice de Corrélation : Analyse de la relation entre le temps, le volume et le taux de croissance.
- Distribution Régionale : Box Plot mettant en évidence les disparités de croissance entre l'Afrique de l'Ouest, l'Est, le Centre, le Nord et le Sud.

#Insights Majeurs (Extraits de INSIGHTS.md)

Explosion Démographique : La population de la zone étudiée a plus que triplé depuis 1960, avec une corrélation quasi-linéaire (0.99) entre l'année et le volume global.
Le Géant Outlier : Le Nigeria est identifié statistiquement comme un outlier majeur, avec une population 10x supérieure à la médiane régionale.
Stabilité de la Croissance : Contrairement aux tendances mondiales, le taux de croissance annuel moyen en Afrique reste solidement ancré au-dessus de 2%.
(Voir le fichier INSIGHTS.md pour l'analyse complète)

#Installation Locale

Pour faire tourner le projet sur votre machine :
Cloner le dépôt :
code
Bash
git clone https://gitlab.formuloo.com/votre-user/mini-projet-afrique.git
cd mini-projet-afrique
Installer les dépendances :
code
Bash
pip install -r requirements.txt
Lancer l'application :
code
Bash
streamlit run app.py

# Structure du Dépôt
app.py : Code principal de l'application Streamlit.
exploration.ipynb : Notebook Jupyter contenant l'EDA et les tests de nettoyage.
africa_population_cleaned.csv : Le dataset final prêt à l'emploi.
requirements.txt : Liste des librairies Python nécessaires.
INSIGHTS.md : Rapport détaillé des conclusions analytiques.
README.md : Documentation actuelle.
Réalisé par TANDAH DJIMELI MARCELLE
