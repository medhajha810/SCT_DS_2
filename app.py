from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('kmeans_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        gender = int(data['gender'])
        age = int(data['age'])
        income = int(data['income'])
        score = int(data['score'])
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Required: gender (0/1), age, income, score.'}), 400
    X = np.array([[gender, age, income, score]])
    X_scaled = scaler.transform(X)
    cluster = int(model.predict(X_scaled)[0])
    return jsonify({'cluster': cluster})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 