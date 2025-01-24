# Task 2: Exploratory Data Analysis (EDA)

## Overview
This task involves a thorough examination of the dataset to understand its structure, distributions, and relationships. The goal is to uncover insights that will guide subsequent steps in the machine learning pipeline.

## Objectives

- **Understand Data Structure:** Determine the number of rows, columns, and data types within the dataset.
- **Summary Statistics:** Calculate central tendency, dispersion, and distribution shapes.
- **Distribution of Features:** Visualize both numerical and categorical feature distributions.
- **Correlation Analysis:** Identify relationships between numerical variables.
- **Identify Missing Values:** Spot and strategize handling of missing data.
- **Detect Outliers:** Use various plots to identify anomalies in the data.

## Data Overview

- **Dataset:** Found in `./data/transactions.csv`
- **Rows:** [Number of rows if known]
- **Columns:** [Number of columns if known]

## Summary Statistics

- **Central Tendency:** Measures like mean, median for numerical features.
- **Dispersion:** Standard deviation, variance.
- **Shape:** Skewness, kurtosis.

## Distribution Analysis

### Numerical Features
- **Histograms:** To show distribution shapes, skewness, and potential outliers.
- **Q-Q Plots:** To check for normality.

### Categorical Features
- **Bar Charts:** To visualize the frequency of categories.

## Correlation Analysis

- **Heatmap:** To illustrate correlations between numerical variables.

## Missing Values

- **Heatmap of Missing Data:** Visual representation of missing data distribution across features.
- **Count of Missing Values:** Numerical summary of missing data.

## Outlier Detection

- **Box Plots:** To identify outliers in numerical features.

## Insights and Decisions

- **Data Quality:** Observations on data integrity, including skewness, outliers, and missing values.
- **Feature Relationships:** Insights into how features correlate with each other.
- **Next Steps:** Decisions on data preprocessing, feature engineering based on EDA findings.

## Jupyter Notebook

- **Location:** `./notebooks/02_exploratory_data_analysis.ipynb`
- **Content:** All EDA steps are documented with code, visualizations, and commentary.

## How to Use

1. **Open Notebook:** Navigate to `./notebooks/` and open `02_exploratory_data_analysis.ipynb` in Jupyter.
2. **Run Cells:** Execute each cell to see the EDA in action or review the results already produced.
3. **Interpret Results:** Use the insights from this notebook to inform your approach in the next tasks.

## References

- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## Next Steps

- **Feature Engineering:** Based on EDA, engineer new features or transform existing ones.
- **Model Building:** Use EDA findings to guide model selection and feature importance.

This task lays the groundwork for a data-driven approach to credit scoring model development. The insights gained here are pivotal for making informed decisions in the subsequent stages of our project.