from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Initialize the Flask app
app = Flask(__name__)

# Load the trained machine learning model
try:
    model_path = '/Users/zelalemtegene/Desktop/week-6/notebooks/gbm_model.pkl'  # Absolute path
    print(f"Loading model from: {model_path}")
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

@app.route('/')
def home():
    return "Welcome to the Machine Learning Model API!"

# Endpoint for health check
@app.route('/health', methods=['GET'])
def health_check():
    if model:
        return jsonify({"status": "API is running and model is loaded!"})
    else:
        return jsonify({"status": "API is running, but model failed to load!"}), 500

# Endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model is not loaded. Cannot make predictions."}), 500

    try:
        # Get JSON data from the POST request
        data = request.get_json()
        
        # Ensure input data is provided
        if 'features' not in data:
            return jsonify({"error": "Missing 'features' in request data."}), 400
        
        # Convert features to a NumPy array and reshape for prediction
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return the prediction result
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on a specific port (default: 5003)
    app.run(debug=True, port=5003)