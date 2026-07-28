# Africa Population Pulse: Streamlit Analytical Dashboard

# Project Overview

This project was developed as part of Sprint S2 during my Master 2 internship at Formuloo.
The objective is to transform raw World Bank data concerning the population of 54 African countries (from 1960 to 2023) into an interactive and visual decision-making tool.
Dashboard Link: https://dashboard-analytique-app-sur-dataset-population-africaine-xdh8.streamlit.app/

# Tech Stack

Language: Python 3.12
Data Analysis: Pandas, NumPy
Visualization: Plotly Express (Interactive charts)
Interface: Streamlit
Deployment: Streamlit Community Cloud

# Data Pipeline (ETL)

The project follows a structured data processing rigor:
Extraction: Retrieval of the "World Development Indicators" dataset from the World Bank.
Transformation (Wide to Long): Reshaping from wide format (years as columns) to long format via the melt method. The dataset expanded from 54 rows to over 3,400 rows.
Cleaning & Enrichment:
Normalization of column names (snake_case).
Missing value handling using median imputation by country.
Outlier detection using the IQR (Interquartile Range) method.
Creation of 10 analytical columns (YoY growth rate, Population in millions, Regions, Decades, etc.).
Loading: Export to an optimized CSV file for the dashboard.

# Dashboard Features

The dashboard provides 5 levels of analytical reading:
- Key Performance Indicators (KPIs): Instant visualization of total filtered population and average growth rate.
- Temporal Analysis: Line chart showing growth trajectories by country.
- Geographic Comparison: Interactive choropleth map of Africa.
- Correlation Matrix: Analysis of the relationship between time, volume, and growth rate.
- Regional Distribution: Box Plot highlighting growth disparities across West, East, Central, North, and Southern Africa.

# Key Insights (Excerpts from INSIGHTS.md)

Demographic Explosion: The population of the studied region has more than tripled since 1960, showing a near-linear correlation (0.99) between year and total volume.
The Outlier Giant: Nigeria is statistically identified as a major outlier, with a population 10x greater than the regional median.
Growth Stability: Contrary to global trends, the average annual growth rate in Africa remains firmly anchored above 2%.
(See the INSIGHTS.md file for the complete analysis)

# Local Installation

To run the project on your local machine:
Clone the repository:
```bash
git clone [https://github.com/Tandah-Marcelle/Dashboard-Analytique-Streamlit-sur-Dataset-Population-Africaine.git](https://github.com/Tandah-Marcelle/Dashboard-Analytique-Streamlit-sur-Dataset-Population-Africaine.git)
cd mini-projet-afrique
