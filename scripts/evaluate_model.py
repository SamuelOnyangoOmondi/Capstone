import pandas as pd
from joblib import load
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Paths for model and dataset
dataset_path = "D:/Capstone/data/plas_tech_complex_gas_production.csv"
model_path = 'D:/Capstone/model/gradient_boosting_model_tuned.joblib'

# Load the dataset
logging.info(f"Loading dataset from {dataset_path}")
data = pd.read_csv(dataset_path)

# Print basic dataset info
logging.info(f"Data loaded successfully with shape: {data.shape}")
logging.info(f"First few rows of the dataset:\n{data.head()}")

# Prepare the test data (features and target)
X_test = data[['Plastic_Waste_Input_kg', 'Operating_Cost_USD', 'Time_of_Production_minutes']]
y_test = data['Gas_Output_liters']
logging.info(f"Features (X) shape: {X_test.shape}")
logging.info(f"Target (y) shape: {y_test.shape}")

# Load the trained model
logging.info(f"Loading the model from {model_path}")
model = load(model_path)

# Make predictions
logging.info("Evaluating the model...")
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Log evaluation metrics
logging.info(f"Mean Absolute Error (MAE): {mae}")
logging.info(f"Mean Squared Error (MSE): {mse}")
logging.info(f"R² Score: {r2}")

# (Optional) Add visualization of true vs predicted values
