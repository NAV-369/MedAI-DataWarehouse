Here’s a professional and well-structured `README.md` for **Task-6**. You can customize it further based on your specific project details.

---

# **Task-6: Machine Learning Model Deployment with Flask**

## **Overview**
This project demonstrates the deployment of a machine learning model using **Flask**, a lightweight web framework for Python. The model is trained to perform a specific task (e.g., classification or regression) and is exposed via a REST API for making predictions. The API provides endpoints for health checks and predictions, making it easy to integrate with other applications.

---

## **Project Structure**
```
task-6/
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask application and API endpoints
│   ├── model/               # Directory for the trained model
│   │   └── gbm_model.pkl    # Serialized Gradient Boosting Model
├── notebooks/
│   └── model_training.ipynb # Notebook for training and saving the model
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── tests/                   # Unit tests for the API
    └── test_api.py
```

---

## **Requirements**
To run this project, you need the following:
- Python 3.8+
- Flask
- Scikit-learn
- Joblib
- NumPy

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## **How to Run the Application**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd task-6
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Flask Application**
```bash
python test/FlaskApi.py
```

The application will start running at `http://127.0.0.1:5003`.

---

## **API Endpoints**

### **1. Health Check**
- **Endpoint:** `/health`
- **Method:** `GET`
- **Description:** Checks if the API is running and the model is loaded.
- **Response:**
  ```json
  {
    "status": "API is running and model is loaded!"
  }
  ```

### **2. Make Predictions**
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Accepts input features and returns predictions.
- **Request Body:**
  ```json
  {
    "features": [feature1, feature2, ...]
  }
  ```
- **Response:**
  ```json
  {
    "prediction": [predicted_value]
  }
  ```

---

## **Example Usage**

### **Health Check**
```bash
curl http://127.0.0.1:50003/health
```

### **Prediction**
```bash
curl -X POST http://127.0.0.1:5003/predict \
-H "Content-Type: application/json" \
-d '{"features": [1.0, 2.0, 3.0, 4.0]}'
```

---

## **Model Training**
The model used in this project was trained using a Gradient Boosting Classifier. The training process is documented in the `notebooks/Model_Serving_Api.ipynb` notebook. Key steps include:
1. Data preprocessing
2. Model training
3. Model evaluation
4. Saving the model using `joblib`

---

## **Testing**
Unit tests for the API are located in the `tests/` directory. Run the tests using:
```bash
python -m pytest tests/
```

---

## **Troubleshooting**

### **1. Model Loading Issues**
- Ensure the model file (`gbm_model.pkl`) 
- Verify that the file path in `FlaskApi.py` is correct.

### **2. Dependency Issues**
- Ensure all dependencies are installed using `pip install -r requirements.txt`.
- If you encounter version conflicts, consider using a virtual environment.

### **3. API Errors**
- Check the Flask logs for detailed error messages.
- Ensure the input data format matches the expected schema.

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---