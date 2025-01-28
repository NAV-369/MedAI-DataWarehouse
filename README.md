# Bati Bank - AI-Driven Credit Scoring Model

### Business Need

You are an Analytics Engineer at Bati Bank, a leading financial service provider with over 10 years of experience. Bati Bank has partnered with an upcoming successful eCommerce company to provide a buy-now-pay-later service, enabling customers to purchase products on credit if they qualify. Your project is to create a Credit Scoring Model using data from the eCommerce platform. This model will estimate the likelihood of a borrower defaulting on a loan, which will help evaluate applicants for the buy-now-pay-later service.

### Credit Scoring Process

Credit scoring involves assigning a quantitative score to a potential borrower, assessing how likely they are to default in the future. The score is built using historical data on previous borrowers and their loan performance. This score can then be used to evaluate new applicants based on the same information.

### References:
	•	Basel II Capital Accord (for loan procedures and default definition)
	•	Credit Scoring Approaches
	•	Credit Scoring Insights

# Task1: Understanding Credit Risk
	•	Focus: Understand the concept of credit risk and its relation to default prediction.
	•	Key Resources:
	•	Basel II Capital Accord
	•	Alternative Credit Scoring
	•	World Bank Credit Scoring Guidelines

# Task2: Exploratory Data Analysis (EDA)
	•	Overview of Data:
	•	Understand dataset structure: rows, columns, and data types.
	•	Summary Statistics: Analyze central tendency, dispersion, and distribution.
	•	Distribution of Features: Visualize numerical and categorical features.
	•	Correlation Analysis: Assess relationships between numerical features.
	•	Missing Values: Identify and plan imputation strategies.
	•	Outlier Detection: Use box plots to identify anomalies.

# Task3: Feature Engineering
	•	Create Aggregate Features:
	•	Examples: Total Transaction Amount, Average Transaction Amount, etc.
	•	Extract Features:
	•	Examples: Transaction Hour, Day, Month, Year.
	•	Encode Categorical Variables:
	•	Techniques: One-Hot Encoding, Label Encoding.
	•	Handle Missing Values:
	•	Strategies: Imputation or Removal.
	•	Normalize/Standardize Numerical Features:
	•	Normalize: Scale features to range [0,1].
	•	Standardize: Scale to mean 0 and standard deviation 1.
	•	Tools:
	•	xverse
	•	woe
	•	Weight of Evidence (WOE) and Information Value (IV) explained.

# Task4: Default Estimator and WoE Binning
	•	Objective: Classify users as high or low risk (default).
	•	Steps:
	•	Visualize transactions in RFMS space.
	•	Establish a boundary for classifying good and bad users.
	•	Perform WoE binning for features using references.
	•	Outcome: Create a default estimator to help in classification.

# Task5: Modeling
	•	Model Selection and Training:
	•	Split data into training and testing sets.
	•	Choose models (e.g., Logistic Regression, Decision Trees, Random Forest, GBM).
	•	Train models on training data.
	•	Hyperparameter Tuning:
	•	Techniques: Grid Search, Random Search.
	•	Model Evaluation:
	•	Metrics: Accuracy, Precision, Recall, F1 Score, ROC-AUC.

# Task6: Model Serving API Call
	•	Create a REST API to serve the trained models for real-time predictions.
	•	Steps:
	•	Choose a framework (e.g., Flask, FastAPI, Django).
	•	Load the trained model.
	•	Define API endpoints to receive data and return predictions.
	•	Deploy the API on a server or cloud platform.

