# Task 2 - Data Cleaning and Transformation

## Data Cleaning

### Removing Duplicates
- Identify and remove any duplicate entries in the dataset to ensure data integrity.

### Handling Missing Values
- Decide on strategies for dealing with missing data, such as imputation, deletion, or flagging for further investigation.

### Standardizing Formats
- Ensure that all data is in a consistent format, particularly for dates, times, and categorical variables.

### Data Validation
- Validate data against expected formats and ranges to catch anomalies or errors.

### Storing Cleaned Data
- After cleaning, save the data in an appropriate format or database for further processing.

#### Database Storage
- Use a database system to store cleaned data efficiently, allowing for easier querying and transformation.

## DBT for Data Transformation

### Setting Up DBT
- **Install DBT**: Install the Data Build Tool for managing data transformations:
  pip install dbt

- **Initialize DBT Project**:
  dbt init my_project

### Defining Models
- Create DBT models for data transformation. DBT models are SQL files that define transformations on your data.

- **Run DBT Models**: 
  dbt run

### Testing and Documentation
- Use DBT’s testing and documentation features to ensure data quality and provide context for the transformations.

- **Run Tests**:
  ```
  dbt test
  ```

- **Generate Documentation**:
  ```
  dbt docs generate
  ```

- **Serve Documentation**:
  ```
  dbt docs serve
  ```

## Monitoring and Logging

### Logging
- Implement logging to track the scraping process, capture errors, and monitor progress.