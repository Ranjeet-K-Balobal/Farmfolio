# app.py

from flask import Flask, request, jsonify
from model import load_and_preprocess_data, train_logistic_regression_model, predict_creditworthiness

app = Flask(__name__)

# Load and preprocess the data
file_path = 'data/credit.csv'  # Adjust the path accordingly
df = load_and_preprocess_data(file_path)

# Train the Logistic Regression model
model, _, _ = train_logistic_regression_model(df)

# Example endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Predict creditworthiness
        prediction, interpreted_prediction = predict_creditworthiness(model, data)

        # Return the prediction as JSON
        result = {'prediction': prediction, 'interpreted_prediction': interpreted_prediction}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
