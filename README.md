# Sydney Rental Value Index (SRVI)

> A data analytics project exploring Sydney's rental market and identifying postcode-level rental value opportunities using Python, SQL, and Tableau.

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-Data%20Analysis-blue)
![Tableau](https://img.shields.io/badge/Tableau-Data%20Visualisation-orange)
![SQL](https://img.shields.io/badge/SQL-Analysis-blue)

---

## Project Overview

Sydney's rental market is expensive and highly variable across different locations and property types.

While renters can easily compare individual property prices, understanding which areas provide the strongest overall rental value is more challenging.

This project analyses Sydney rental data and develops a **Sydney Rental Value Index (SRVI)** to identify postcode-level rental value opportunities.

The project follows an end-to-end analytics workflow, including:

- Data cleaning and validation
- Exploratory data analysis
- Rental market analysis
- Rental Value Index development
- SQL analysis
- Interactive Tableau dashboard development

---

# Business Problem

Sydney renters face significant differences in rental prices depending on location and property characteristics.

A high rental price does not necessarily mean poor value, and a low rental price does not automatically represent the best opportunity.

The key question explored in this project is:

> **Which Sydney postcodes provide the strongest rental value opportunities?**

To investigate this, the project analyses rental prices and market availability to develop a postcode-level Rental Value Index.

---

# Objectives

The main objectives of this project are to:

- Analyse Sydney's rental market using real rental data
- Clean and validate a large residential rental dataset
- Investigate rental prices across postcodes
- Analyse rental prices by number of bedrooms
- Identify postcode-level rental value opportunities
- Develop a Sydney Rental Value Index (SRVI)
- Build an interactive Tableau dashboard
- Communicate insights through data visualisation

---

# Dataset

The project uses the:

**NSW Fair Trading Residential Rental Bond Lodgements Year 2025 dataset**

The dataset contains residential rental information used to analyse rental prices and market activity across Sydney.

Key fields used during the analysis include:

- Lodgement Date
- Postcode
- Dwelling Type
- Bedrooms
- Weekly Rent

The data was cleaned and processed using Python before being used for further analysis and visualisation.

---

# Data Cleaning and Preparation

The raw dataset required cleaning and validation before analysis.

The data preparation process included:

- Standardising column names
- Selecting relevant variables
- Checking for missing values
- Identifying duplicate records
- Cleaning rental price information
- Preparing postcode-level rental data
- Creating analysis-ready datasets for visualisation

The processed dataset was then used to calculate rental market metrics and develop the Rental Value Index.

---

# Rental Value Index (SRVI)

The **Sydney Rental Value Index (SRVI)** is designed to identify rental opportunities by comparing rental affordability and market availability across different postcodes.

The index allows rental markets to be compared beyond simply looking at rental prices.

A postcode with a stronger Rental Value Score represents a potentially more attractive rental opportunity relative to other locations in the dataset.

The SRVI is used throughout the Tableau dashboard to identify and visualise the strongest rental value opportunities.

---

# Key Insights

The analysis highlights several important patterns in Sydney's rental market:

- Rental prices vary significantly across different postcodes.
- Rental value cannot be evaluated using weekly rent alone.
- Some postcodes provide stronger rental value opportunities when affordability and market activity are considered together.
- Rental prices generally increase as the number of bedrooms increases.
- The number of available rental listings varies significantly across the market.
- The Rental Value Index helps identify high-value postcode-level opportunities.

---

# Interactive Dashboard

The project includes an interactive Tableau dashboard designed to provide an executive-level view of Sydney's rental market.

The dashboard includes:

### Key Performance Indicators

- Average Weekly Rent
- Total Listings
- Average SRVI

### SRVI Map

A geographical visualisation showing rental market activity across Sydney postcodes.

### Top Rental Value Opportunities

A ranked view of postcodes with the strongest Rental Value Scores.

### Rent by Bedrooms

A comparison of rental prices across different bedroom counts.

### Rental Value vs Market Availability

A scatter plot showing the relationship between rental prices, market activity, and rental value opportunities.

The dashboard also includes interactive filtering, allowing users to explore rental opportunities by postcode.

---

## Tableau Dashboard

**View the interactive dashboard on Tableau Public:**

[Add your Tableau Public Dashboard Link Here](https://public.tableau.com/app/profile/adi.raje8198/viz/sydney_rental_value_index/Dashboard1))

---

# Tech Stack

| Category | Tools Used |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database / Querying | SQL |
| Visualisation | Tableau Public |
| Version Control | Git & GitHub |

---

# Project Workflow

```text
Raw Rental Data
       ↓
Python Data Cleaning
       ↓
Data Validation
       ↓
Exploratory Data Analysis
       ↓
Rental Market Analysis
       ↓
Rental Value Index
       ↓
SQL Analysis
       ↓
Tableau Dashboard
