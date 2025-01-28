# Task 5: Modelling

## Overview
This task focuses on selecting, training, tuning, and evaluating machine learning models for credit risk assessment. We aim to predict the likelihood of default by leveraging the features engineered in previous tasks.

## Objectives

- **Model Selection:** Choose and implement at least two models from Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting Machines (GBM).
- **Data Splitting:** Divide the dataset into training and testing sets to assess model performance on unseen data.
- **Model Training:** Train selected models on the training data.
- **Hyperparameter Tuning:** Optimize model performance through:
  - **Grid Search:** Exhaustive search over specified parameter values.
  - **Random Search:** Random sampling from a distribution of parameter values.
- **Model Evaluation:** Measure model effectiveness using various metrics including:
  - **Accuracy:** Proportion of correct predictions among the total number of cases.
  - **Precision:** Ratio of true positive predictions to the total predicted positives.
  - **Recall:** Ratio of true positive predictions to all actual positives.
  - **F1 Score:** Harmonic mean of precision and recall, providing a balance between them.
  - **ROC-AUC:** Measures the ability of the classifier to distinguish between classes.

## Implementation Details

### **Data Preparation**
- Ensure data is preprocessed (encoded, scaled, etc.) before splitting into training and test sets.

### **Model Selection and Training**

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    'Random Forest': RandomForestClassifier(random_state=42),
    'GBM': GradientBoostingClassifier(random_state=42)
}

Hyperparameter Tuning
Grid Search Example (Random Forest)
python
rf_param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}
rf_grid_search = GridSearchCV(RandomForestClassifier(random_state=42), rf_param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
rf_grid_search.fit(X_train, y_train)

Random Search Example (Random Forest)
python
rf_param_dist = {
    'n_estimators': [int(x) for x in np.linspace(start=200, stop=2000, num=10)],
    'max_features': ['sqrt', 'log2'],
    # ... other parameters
}
rf_random_search = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_distributions=rf_param_dist, n_iter=100, cv=3, scoring='roc_auc', random_state=42, n_jobs=-1)
rf_random_search.fit(X_train, y_train)

Model Evaluation
python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_model(model, X_test, y_test):
    # ... evaluation logic ...

for name, model in models.items():
    evaluate_model(model, X_test, y_test)

How to Use
Jupyter Notebook: Navigate to ./notebooks/05_modelling.ipynb to see or run the code for this task.
Data: Ensure all features have been engineered and properly preprocessed before running model experiments.

Next Steps
Model Deployment: Prepare the best performing model for deployment into a production environment.
Model Monitoring: Establish metrics and checks for model performance in real-world scenarios.

References
Scikit-learn Documentation (link_to_sklearn_docs)
Hyperparameter Tuning (link_to_hyperparameter_tuning)

This task establishes which models perform best in predicting credit risk, setting the stage for model deployment and continuous improvement.

So RESULT:
Comparison of Metrics:
Model               Accuracy  Precision Recall    F1 Score  ROC AUC   
----------------------------------------------------------------------
Random Forest       0.9980    0.0000    0.0000    0.0000    0.9315    
GBM                 0.9980    0.0000    0.0000    0.0000    0.9368    

Best Model: GBM (Based on ROC AUC)
GBM Metrics: {'Accuracy': 0.9980487124986933, 'Precision': 0.0, 'Recall': 0.0, 'F1 Score': 0.0, 'ROC AUC': np.float64(0.9368235694585065)}

```