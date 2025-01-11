from flask import Flask, request, jsonify
import pandas as pd
import joblib
import csv
from datetime import datetime

# Load the trained model
model = joblib.load("../modelo/glm_optimized.pkl")

# Create the Flask application
app = Flask(__name__)

# Route to receive the file and make the prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the file was sent in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        
        # Check if a file was selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        # Read the CSV file (or any other type of file you're using)
        df = pd.read_csv(file)
        
        # Make the prediction with the loaded model
        prediction = model.predict(df)
        
        # Save the request and prediction in a CSV file
        with open('predictions_log.csv', mode='a', newline='') as file_log:
            writer = csv.writer(file_log)
            # Save the date, the received file, and the prediction
            writer.writerow([datetime.now(), file.filename, prediction.tolist()])
        
        # Return the prediction as a response
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Start the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
