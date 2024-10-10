import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from joblib import load
from sklearn.metrics import mean_absolute_error

# Load the dataset
dataset_path = "D:/Capstone/data/plas_tech_complex_gas_production.csv"
data = pd.read_csv(dataset_path)

# ----- Part 1: Feature Correlations with the Target (Gas Output) -----
print("Visualizing feature correlations with Gas Output")

# Create a pairplot to visualize the relationship between features and the target (Gas_Output_liters)
sns.pairplot(data, x_vars=['Plastic_Waste_Input_kg', 'Operating_Cost_USD', 'Time_of_Production_minutes'],
             y_vars='Gas_Output_liters', height=5, aspect=1, kind='scatter')

plt.title('Feature Correlations with Gas Output')
plt.tight_layout()
plt.show()

# ----- Part 2: True vs. Predicted Values Plot -----
print("Visualizing true vs. predicted values")

# Load the trained model
model_path = 'D:/Capstone/model/gradient_boosting_model_tuned.joblib'
model = load(model_path)

# Prepare the test data (features and target)
X_test = data[['Plastic_Waste_Input_kg', 'Operating_Cost_USD', 'Time_of_Production_minutes']]
y_test = data['Gas_Output_liters']

# Make predictions
y_pred = model.predict(X_test)

# Plot True vs. Predicted values
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs True Values')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Perfect Fit')
plt.xlabel('True Gas Output')
plt.ylabel('Predicted Gas Output')
plt.title('True vs. Predicted Gas Output')
plt.legend()
plt.show()

# Calculate and print Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
