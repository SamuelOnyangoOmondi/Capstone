from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Load the trained model from the Docker container's filesystem
model_path = '/app/model/gradient_boosting_model_tuned.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model not found at {model_path}")

# Home route to display a form for input
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the form data from the user
        plastic_waste = float(request.form['Plastic_Waste_Input_kg'])
        operating_cost = float(request.form['Operating_Cost_USD'])
        production_time = float(request.form['Time_of_Production_minutes'])
        
        # Prepare the data for prediction
        input_data = [[plastic_waste, operating_cost, production_time]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Render the result on the page
        return render_template('index.html', prediction=prediction[0])

    # If GET method, just show the form
    return render_template('index.html', prediction=None)

# Predict route for API access (useful for testing via Postman or cURL)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = [[
        data['Plastic_Waste_Input_kg'], 
        data['Operating_Cost_USD'], 
        data['Time_of_Production_minutes']
    ]]
    prediction = model.predict(input_data)
    return jsonify({'gas_output_liters': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
