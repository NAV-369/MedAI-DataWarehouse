# Task 4: Default Estimator and WoE Binning

## Purpose
The goal of this task is to create a system for classifying customers into high-risk and low-risk categories based on their transaction history, utilizing the RFMS (Recency, Frequency, Monetary, Score) framework. We also apply Weight of Evidence (WoE) binning to enhance feature predictive power for credit risk modeling.

## Objectives

- **Construct a Default Estimator:** Use RFMS components to classify customers as 'Good' or 'Bad' in terms of default risk.
- **Visualize RFMS Space:** Identify natural boundaries for risk classification.
- **Assign Risk Labels:** Based on RFMS scores, label users as high or low risk.
- **Perform WoE Binning:** Transform features using WoE to improve model interpretability and performance.

## RFMS Components

### Calculation
- **Recency:** Days since the last transaction.
- **Frequency:** Number of transactions.
- **Monetary:** Total amount spent.
- **Score:** A composite score based on R, F, and M.

```python
# Example code for calculating RFMS components
df['Recency'] = (max_date - df.groupby('AccountId')['TransactionDate'].transform('max')).dt.days
df['Frequency'] = df.groupby('AccountId')['TransactionId'].transform('count')
df['Monetary'] = df.groupby('AccountId')['Amount'].transform('sum')
df['Score'] = df['Recency'] + df['Frequency'] + df['Monetary']  # Example of scoringw