# Task 1: Understanding Credit Risk

## Project Overview
This document outlines the objectives and deliverables for Task 1 of the AI Mastery Course focused on understanding the concept of credit risk for Bati Bank's buy-now-pay-later initiative.

## Objective
The primary goal is to gain a comprehensive understanding of credit risk, including its definitions, implications, and management strategies within the banking sector.

## Key Concepts

### Credit Scoring
- **Definition:** A method to assess the creditworthiness of potential borrowers by assigning a numerical score based on their financial behavior.
- **Purpose:** To predict the likelihood of default.

### Default
- **Definition:** When a borrower fails to repay a loan according to the agreed terms.
- **Contextual Variation:** Definitions can vary but must comply with financial regulations like Basel II.

### Basel II Capital Accord
- **Overview:** A framework for banking supervision which emphasizes capital adequacy, supervisory review, and market discipline.
- **Pillars:**
  - Pillar 1: Minimum Capital Requirements
  - Pillar 2: Supervisory Review Process
  - Pillar 3: Market Discipline

## Business Implications

### Risk Management
- Enables banks to mitigate losses by identifying high-risk customers early.

### Customer Segmentation
- Allows for tailored credit offerings based on assessed risk, enhancing customer satisfaction and profitability.

### Regulatory Compliance
- Ensures that credit scoring practices are in line with international standards, reducing legal risks.

### Profitability
- Helps in pricing credit products appropriately to balance risk and return.

## Learning Outcomes

- **Conceptual Understanding:** Grasp the foundational concepts of credit risk.
- **Regulatory Awareness:** Recognize the importance of regulatory frameworks like Basel II in credit practices.
- **Strategic Application:** Apply theoretical knowledge to practical business scenarios, particularly in product development for credit services.

## Task Deliverables

- **Report:** A detailed report or notebook documenting the study of credit risk concepts, regulatory frameworks, and their business impacts.
- **Jupyter Notebooks:** Located in `./notebooks/`, these will include:
  - Exploratory data analysis related to credit risk if applicable.
  - Code examples or visualizations to illustrate concepts.

## References

- Basel II Capital Accord - [Link to document]
- Investopedia - [Credit Risk]
- Corporate Finance Institute - [Credit Risk Management]

## How to Use

1. **Navigate to Notebooks:** Go to the `./notebooks/` directory to find the Jupyter notebooks related to this task.
2. **Run the Notebooks:** Use Jupyter Notebook or JupyterLab to open and run `01_understanding_credit_risk.ipynb`.
3. **Review the Report:** Check the report section in this README or in a separate document for a comprehensive overview of credit risk understanding.

## Next Steps

- Proceed to Task 2 for Exploratory Data Analysis to apply this understanding to real data.
- Consider how this knowledge informs feature engineering and model building in subsequent tasks.

This task sets the stage for all credit-related analysis in this project, providing a solid foundation for the technical work to follow.

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


Here's the README.md for Task 3: Feature Engineering formatted with # for headings:

markdown

# Task 3: Feature Engineering

## Overview
Feature engineering transforms raw data into more predictive features, crucial for enhancing model performance in credit risk assessment.

## Objectives

- Create aggregate features to summarize customer behavior.
- Extract time-based features to capture temporal patterns.
- Encode categorical variables for machine learning compatibility.
- Handle missing values to maintain data quality.
- Normalize or standardize numerical features for consistent scaling.
- Implement WOE and IV for feature transformation and selection.

## Implementation Details

### # Create Aggregate Features
- **Total Transaction Amount:** Sum of transactions per customer.
  ```python
  df['TotalTransactionAmount'] = df.groupby('AccountId')['Amount'].transform('sum')
Average Transaction Amount: Mean transaction amount per customer.
python
df['AverageTransactionAmount'] = df.groupby('AccountId')['Amount'].transform('mean')
Transaction Count: Number of transactions per customer.
python
df['TransactionCount'] = df.groupby('AccountId')['TransactionId'].transform('count')
Standard Deviation of Transaction Amounts: Variability in transaction amounts.
python
df['StdTransactionAmount'] = df.groupby('AccountId')['Amount'].transform('std')

# Extract Features
Time-Based Features: From transaction timestamps for pattern analysis.
python
df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])
df['TransactionHour'] = df['TransactionStartTime'].dt.hour
df['TransactionDay'] = df['TransactionStartTime'].dt.day
df['TransactionMonth'] = df['TransactionStartTime'].dt.month
df['TransactionYear'] = df['TransactionStartTime'].dt.year

# Encode Categorical Variables
One-Hot Encoding: For ChannelId.
python
df = pd.get_dummies(df, columns=['ChannelId'], prefix=['Channel'])
Label Encoding: For ProductCategory when necessary.
python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['ProductCategory_encoded'] = le.fit_transform(df['ProductCategory'])

# Handle Missing Values
Imputation: Mean or mode strategy.
python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
df[numerical_columns] = imputer.fit_transform(df[numerical_columns])
Removal: If the missing data is insignificant.

# Normalize/Standardize Numerical Features
Normalization: To scale between 0 and 1.
python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])
Standardization: To center around 0 with unit variance.
python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Feature Engineering with WOE and IV
Weight of Evidence (WOE) and Information Value (IV): For feature enhancement and selection.
python
def woe_iv(X, y, event=1):
    # Simplified WOE/IV calculation
    ...
X = df['ProductCategory']
y = df['FraudResult']
woe_df = woe_iv(X, y)
df = df.merge(woe_df['WOE'], left_on='ProductCategory', right_index=True, how='left', suffixes=('', '_WOE'))

### How to Use
Jupyter Notebook: Execute ./notebooks/03_feature_engineering.ipynb for this task's code.
Interpret: Review visualizations and statistics for insights.

### Next Steps
Model Training: Utilize these features in credit risk models.
Feature Selection: Prioritize based on IV for model inclusion.

### References
WOE and IV Explanation (link_to_woe_iv_explanation)
Feature Engineering Techniques (link_to_feature_engineering)

```