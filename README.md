# Sydney Rental Value Index (SRVI)

> An end-to-end data analytics project exploring Sydney's rental market and identifying postcode-level rental value opportunities using rental pricing data and an interactive Tableau dashboard.

---

## Overview

Sydney's rental market varies significantly across different postcodes and property types.

A lower rent does not always mean better value, and higher-priced areas may offer different market characteristics.

This project analyses Sydney rental data to develop a **Sydney Rental Value Index (SRVI)** and identify areas that may represent strong rental value opportunities.

The analysis combines rental prices, listing activity and postcode-level metrics to make Sydney's rental market easier to explore.

---

# Business Problem

Rental prices alone do not provide a complete picture of market value.

The key question explored in this project is:

> **Which Sydney postcodes provide the strongest rental value opportunities?**

To answer this, the project analyses rental prices and market activity across Sydney postcodes and develops a Rental Value Index (SRVI).

---

# Project Objectives

- Clean and prepare a large Sydney rental dataset
- Analyse rental prices across postcodes and dwelling characteristics
- Identify patterns in rental prices and market activity
- Develop a postcode-level Rental Value Index (SRVI)
- Identify high-value rental opportunities
- Build an interactive Tableau dashboard
- Present insights through data visualisation

---

# Dataset

The project uses NSW residential rental bond lodgement data.

The raw dataset was processed using Python to prepare it for analysis.

### Key fields used

- Lodgement Date
- Postcode
- Dwelling Type
- Bedrooms
- Weekly Rent

The processed dataset contains more than **280,000 rental records** used for analysis and visualisation.

---

# Data Processing

The dataset was cleaned and prepared using Python and Pandas.

Key processing steps included:

- Loading and inspecting the raw dataset
- Selecting relevant analytical variables
- Standardising column names
- Handling missing and invalid values
- Identifying duplicate records
- Preparing rental data for analysis
- Creating a cleaned dataset for downstream analysis

---

# Rental Value Index (SRVI)

The **Sydney Rental Value Index (SRVI)** is designed to provide a comparative measure of rental value across Sydney postcodes.

The index is used to explore the relationship between:

- Rental affordability
- Rental market activity
- Postcode-level rental patterns

Higher-value opportunities are highlighted to help identify postcodes with stronger relative rental value.

---

# Exploratory Analysis

The analysis explores several key questions:

### Rental prices by postcode

Which Sydney postcodes have the highest and lowest rental prices?

### Rental prices by number of bedrooms

How does weekly rent change as the number of bedrooms increases?

### Rental value opportunities

Which postcodes achieve the strongest Rental Value Index scores?

### Market availability

How does rental market activity vary across different rent levels and locations?

---

# Tableau Dashboard

An interactive Tableau dashboard was developed to communicate the main findings.

## Dashboard Features

### Key Performance Indicators

- Average Weekly Rent
- Total Listings
- Average SRVI

### SRVI Map

An interactive map showing rental market activity across Sydney.

### Top 10 Rental Value Opportunities

A ranking of postcodes with the strongest rental value scores.

### Rent by Bedrooms

A comparison of rental prices across different bedroom counts.

### Rental Value vs Market Availability

A scatter plot exploring the relationship between adjusted rent and listing activity.

### Interactive Filtering

Selecting locations on the map updates relevant dashboard visualisations.

---

# Tech Stack

| Category | Tools |
|----------|-------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Processing | Python ETL |
| Database | PostgreSQL |
| Querying | SQL |
| Visualisation | Tableau Public |
| Version Control | Git & GitHub |

---
# Project Structure

```text
sydney-rental-value-index/
│
├── data/
│   └── processed/        # Cleaned rental datasets
│
├── python/               # Python ETL and analysis scripts
│
├── sql/                  # SQL queries
│
├── reports/              # Project reports and analysis
│
├── docs/                 # Documentation
│
├── README.md
├── requirements.txt
└── .gitignore
